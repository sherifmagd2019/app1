import unittest
from django.urls import reverse
from django.test import Client
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_blog(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["newpost"] = "newpost"
    defaults.update(**kwargs)
    return Blog.objects.create(**defaults)


class BlogViewTest(unittest.TestCase):
    '''
    Tests for Blog
    '''
    def setUp(self):
        self.client = Client()

    def test_list_blog(self):
        url = reverse('blog_blog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_blog(self):
        url = reverse('blog_blog_create')
        data = {
            "name": "name",
            "newpost": "newpost",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_blog(self):
        blog = create_blog()
        url = reverse('blog_blog_detail', args=[blog.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_blog(self):
        blog = create_blog()
        data = {
            "name": "name",
            "newpost": "newpost",
        }
        url = reverse('blog_blog_update', args=[blog.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


