from django.contrib.auth.forms import UserCreationForm

from user.models import User


# class WorkerCreateForm(StyleFormMixin, UserCreationForm):
class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "position",
        )
        # attrs = StyleFormMixin.Meta.attrs