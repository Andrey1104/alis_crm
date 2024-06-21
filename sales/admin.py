from django.contrib import admin
from .models import Company, Contact, Customer, Order
from .forms import OrderAdminForm


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('number',)
        return self.readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.status != 'ON_HOLD':
            form.base_fields['on_hold_reason'].widget.attrs['readonly'] = True
        return form


admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
