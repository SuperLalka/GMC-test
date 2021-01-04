from rest_framework import viewsets
from rest_framework import permissions as drf_permissions

from . import models, permissions, serializers


permission_classes_by_action = {
        'create': [permissions.AdminPermission],
        'retrieve': [drf_permissions.IsAuthenticated],
        'list': [drf_permissions.IsAuthenticated],
        'update': [permissions.AdminPermission],
        'partial_update': [permissions.AdminPermission],
        'destroy': [permissions.AdminPermission]
    }


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'id'

    permission_classes = [drf_permissions.IsAuthenticated]

    def get_permissions(self):
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    lookup_field = 'id'

    permission_classes = [drf_permissions.IsAuthenticated]

    def get_permissions(self):
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
