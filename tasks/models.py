from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # if user is deleted then all the tasks related to that user will be deleted
        related_name="tasks"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title