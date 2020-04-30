from django.urls import path, include
from rest_framework import routers
from .views import HotelViewSet, FavoriteViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r"reviews", ReviewViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"", HotelViewSet)

urlpatterns = router.urls
