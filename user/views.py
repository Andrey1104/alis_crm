from django.views import generic

from user.forms import WorkerCreateForm
from user.models import User


class UserCreateView(generic.CreateView):
    model = User
    form_class = WorkerCreateForm
    # template_name = "task_manager/worker/worker_form.html"
