import calendar

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from user.models import User
from .models import Event
from datetime import datetime, timedelta


class CalendarView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "includes/calendar.html"
    context_object_name = 'events'

    def get_queryset(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        user_id = self.request.GET.get('user_id')
        if user_id:
            selected_user = User.objects.get(id=user_id)
            events = Event.objects.filter(start_time__date__gte=start_of_week,
                                          start_time__date__lte=end_of_week,
                                          user=selected_user)
        else:
            events = Event.objects.filter(start_time__date__gte=start_of_week,
                                          start_time__date__lte=end_of_week)
        return events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        days_of_week = [(start_of_week + timedelta(days=i)).strftime('%A %d') for i in range(7)]
        users = User.objects.all()
        user_id = self.request.GET.get('user_id')
        selected_user = User.objects.get(id=user_id) if user_id else None
        context.update({
            'days_of_week': days_of_week,
            'start_of_week': start_of_week,
            'users': users,
            'selected_user': selected_user,
        })
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'includes/calendar.html'
    success_url = reverse_lazy('task:calendar')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'includes/event_detail.html'
    context_object_name = 'event'


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'includes/event_form.html'
    success_url = reverse_lazy('task:calendar')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'includes/event_confirm_delete.html'
    success_url = reverse_lazy('task:calendar')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.user



# class TaskListView(LoginRequiredMixin, SearchMixin, generic.ListView):
#     model = Task
#     paginate_by = 4
#     template_name = "task_manager/task/task_list.html"
#     search_form_class = TaskSearchForm
#     search_fields = ["name"]
#     queryset = Task.objects.select_related("task_type").prefetch_related(
#         "assignees", "teams", "tags"
#     )
#
#
# class TaskDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Task
#     form_class = MessageForm
#     template_name = "task_manager/task/task_detail.html"
#
#     def get_context_data(self, **kwargs) -> dict:
#         context = super(TaskDetailView, self).get_context_data(**kwargs)
#         task = self.get_object()
#         messages = task.messages.select_related()
#         context["messages"] = messages
#         context["message_form"] = MessageForm()
#         return context
#
#
# class TaskCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Task
#     form_class = TaskCreateForm
#     success_url = reverse_lazy("task:task_list")
#     template_name = "task_manager/task/task_form.html"
#
#
# class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Task
#     form_class = TaskUpdateForm
#     success_url = reverse_lazy("task:task_list")
#     template_name = "task_manager/task/task_form.html"
#
#
# class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Task
#     template_name = "task_manager/task/task_delete.html"
#     success_url = reverse_lazy("task:task_list")
#
#
# class TaskStatusUpdateView(LoginRequiredMixin, SingleObjectMixin, View):
#     model = Task
#     template_name = "task_manager/task/task_form.html"
#
#     @staticmethod
#     def post(request, *args, **kwargs):
#         task_id = kwargs.get("pk")
#         task = Task.objects.get(pk=task_id)
#         if not task.is_completed:
#             task.is_completed = True
#         else:
#             task.is_completed = False
#         task.save()
#         if request.GET.get("next"):
#             cache.clear()
#             return HttpResponseRedirect(request.GET["next"])
#         else:
#             return HttpResponseRedirect(
#                 reverse_lazy("task:task_detail", args=[task_id])
#             )