from rest_framework import routers
from django.urls import path
from .views import VideoViewSet
from .models import Video

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'video', VideoViewSet, base_name='video')

urlpatterns = router.urls
