from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from constants import ORDER_STATUSES, PRODUCTION_STATUS, REASONS, SALUT
from stock.models import Product


class Contact(models.Model):
    salutation = models.CharField(max_length=100, choices=SALUT, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.phone and not self.email:
            raise ValidationError("Either phone or email must be set.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    delivery_address = models.CharField(max_length=255)
    invoice_address = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(max_length=25, unique=True, blank=True)
    status = models.CharField(max_length=25, choices=ORDER_STATUSES)
    production_status = models.CharField(max_length=25, choices=PRODUCTION_STATUS, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    internal_deadline = models.DateField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)
    partner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    end_user = models.CharField(max_length=50, blank=True, null=True)
    direct_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    on_hold_reason = models.CharField(max_length=25, blank=True, null=True, choices=REASONS)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if not self.number:
            current_year = now().year
            last_two_digits = str(current_year)[-2:]
            prefix = f"Z{last_two_digits}"

            last_order = Order.objects.filter(number__startswith=prefix).order_by('-number').first()
            if last_order:
                last_number = int(last_order.number[-5:])
                new_number = last_number + 1
            else:
                new_number = 1

            self.number = f"{prefix}{new_number:05d}"

        if self.deadline and not self.internal_deadline:
            self.internal_deadline = self.deadline - timedelta(weeks=1)

        if self.status == "ON_HOLD" and not self.on_hold_reason:
            raise ValidationError("Reason must be provided if status is 'On hold'.")

        if not self.partner and not self.direct_customer:
            raise ValidationError('Either a partner or a direct customer must be set.')
        if self.partner and self.direct_customer:
            raise ValidationError('Both partner and direct customer cannot be set simultaneously.')

        super().save(*args, **kwargs)


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("product",)

    def __str__(self):
        return f"{self.order}: {self.product} - {self.quantity}"


