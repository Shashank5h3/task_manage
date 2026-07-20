from rest_framework import filters, permissions, viewsets

from .filters import TaskFilter
from .models import Task
from .permissions import IsAdminOrOwner
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrOwner,
    ]

    filterset_class = TaskFilter

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "due_date",
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Task.objects.all()

        if user.groups.filter(name="Admin").exists():
            return Task.objects.all()

        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        