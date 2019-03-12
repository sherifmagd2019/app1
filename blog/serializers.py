from . import models

from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'newpost', 
        )


