from django.urls import path, include

from .views import CommentViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CommentViewSets, basename='comment')

urlpatterns = [
    path("", include(router.urls))
]