from django.contrib import admin
from django import forms
from .models import Blog

class BlogAdminForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'newpost']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'newpost']

admin.site.register(Blog, BlogAdmin)


