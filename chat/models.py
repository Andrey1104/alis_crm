from django.db import models

from alis_crm import settings
from sales.models import Order


class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    text = models.TextField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="messages"
    )
    tag = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tag_messages",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.author}: \n {self.text} \n {self.created_at}"
