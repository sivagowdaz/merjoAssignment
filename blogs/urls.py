from django.urls import path, include

from .views import BlogPostViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BlogPostViewSets, basename='blog')

urlpatterns = [
    path("", include(router.urls))
]