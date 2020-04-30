from rest_framework import viewsets, filters
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .permissions import IsOwner
from .serializers import (
    HotelSerializer,
    FavoriteSerializer,
    ReviewSerializer,
)
from .models import Hotel, Favorite, Review


class HotelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "address", "geolocation"]
    filter_backends = (filters.SearchFilter,)
    queryset = Hotel.objects.all().order_by("name")
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["create", "delete", "put", "update"]:
            self.permission_classes = [IsAdminUser]
        return super(self.__class__, self).get_permissions()


class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
