from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'blog', api.BlogViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Blog
    path('blog/blog/', views.BlogListView.as_view(), name='blog_blog_list'),
    path('blog/blog/create/', views.BlogCreateView.as_view(), name='blog_blog_create'),
    path('blog/blog/detail/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_blog_detail'),
    path('blog/blog/update/<slug:slug>/', views.BlogUpdateView.as_view(), name='blog_blog_update'),
)

