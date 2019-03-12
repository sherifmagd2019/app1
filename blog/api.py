from . import models
from . import serializers
from rest_framework import viewsets, permissions


class BlogViewSet(viewsets.ModelViewSet):
    """ViewSet for the Blog class"""

    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


