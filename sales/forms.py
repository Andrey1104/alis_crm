from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["on_hold_reason"].required = False
        if self.instance and self.instance.status == "ON_HOLD":
            self.fields["on_hold_reason"].required = True

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        on_hold_reason = cleaned_data.get("on_hold_reason")

        if status == "ON_HOLD" and not on_hold_reason:
            self.add_error(
                "on_hold_reason", 
                "Reason must be provided if status is ON_HOLD."
            )

        return cleaned_data


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["number"]

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("production_status")
        on_hold_reason = cleaned_data.get("on_hold_reason")

        if status == "ON_HOLD" and not on_hold_reason:
            self.add_error(
                "on_hold_reason",
                'Reason must be provided if status is "On hold".')
        elif status != "ON_HOLD" and on_hold_reason:
            self.add_error(
                "on_hold_reason",
                'On hold reason can not be chosen when status is not "ON HOLD".'
            )


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'production_status', 'deadline', 'internal_deadline', 'partner', 'end_user', 'direct_customer', 'on_hold_reason']
