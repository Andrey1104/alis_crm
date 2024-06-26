from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Order


@receiver(post_save, sender=Order)
def notify_user_on_order_creation(sender, instance, created, **kwargs):
    if created:
        user_id = 1
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                "type": "notify",
                "message": f"Новий ордер створено з ID {instance.pk}"
            }
        )
