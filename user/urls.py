from django.urls import path

from user.views import UserCreateView

app_name = "user"

urlpatterns = [
    # path("users/", WorkerListView.as_view(), name="worker_list"),
    # path(
    #     "users/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"
    # ),
    # path(
    #     "users/<int:pk>/delete/",
    #     WorkerDeleteView.as_view(),
    #     name="worker_delete",
    # ),
    # path(
    #     "users/<int:pk>/update/",
    #     WorkerUpdateView.as_view(),
    #     name="worker_update",
    # ),
    path("users/create/", UserCreateView.as_view(), name="user_create"),
    # path(
    #     "workers/<int:pk>/worker_task_add/",
    #     WorkerTaskAddView.as_view(),
    #     name="worker_task_add",
    # ),
    # path(
    #     "workers/<int:worker_pk>/<int:task_pk>/task_delete/",
    #     WorkerTaskDeleteView.as_view(),
    #     name="worker_task_delete",
]