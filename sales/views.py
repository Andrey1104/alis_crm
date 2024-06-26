from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView

from chat.forms import ChatCreateForm, MessageForm
from chat.models import Message
from sales.forms import OrderCreateForm
from sales.models import Order
from task.models import Task, Event
from user.models import User


@login_required
def index(request: HttpRequest) -> HttpResponse:
    form = ChatCreateForm()
    user = User.objects.get(id=request.user.id)
    tasks = Task.objects.filter(executor=user)
    events = Event.objects.all()
    context = {
        "form": form,
        "tasks": tasks,
        'events': events
    }
    return render(request, "layouts/index.html", context)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 20
    context_object_name = 'orders'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return Order.objects.filter(Q(number__icontains=search_query))
        return Order.objects.all()


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('sale:order_list')


def projection_view(request):
    return render(request, 'projection/index.html')


# class MessageCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Message
#     form_class = MessageForm
#     template_name = "task_manager/task/task_detail.html"
#
#     def form_valid(self, form: MessageForm) -> HttpResponse:
#         author_pk = self.kwargs.get("pk_author")
#         task_pk = self.kwargs.get("pk_task")
#
#         user = get_object_or_404(User, pk=author_pk)
#         task = get_object_or_404(Task, pk=task_pk)
#
#         form.instance.author = user
#         form.instance.task = task
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         task_pk = self.kwargs.get("pk_task")
#         return reverse_lazy("task:task_detail", args=[task_pk])
#
#
# class MessageDeleteView(LoginRequiredMixin, generic.UpdateView):
#     def get(self, request, *args, **kwargs):
#         task_pk = self.kwargs.get("task_pk")
#         message_pk = self.kwargs.get("message_pk")
#         message = get_object_or_404(Message, pk=message_pk)
#         message.delete()
#         return HttpResponseRedirect(
#             reverse_lazy("task:task_detail", args=[task_pk])
#         )
#
#
# class ChatCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Task
#     form_class = MessageForm
#
#     def post(self, request, *args, **kwargs):
#         task_id = request.POST.get("task")
#         return HttpResponseRedirect(
#             reverse_lazy("task:task_detail", args=[task_id])
#         )