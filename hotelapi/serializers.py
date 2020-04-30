from collections import OrderedDict
from rest_framework import serializers
from django.db.models import Count
from django.db.models import Avg
from .models import Hotel, Favorite, Review


class HotelSerializer(serializers.ModelSerializer):
    hotel_reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
            "address",
            "geolocation",
            "description",
            "image",
            "overall_rating",
            "hotel_reviews",
        )


class FavoriteSerializer(serializers.ModelSerializer):

    hotel = HotelSerializer(read_only=True)
    hotel_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source="hotel", queryset=Hotel.objects.all()
    )

    class Meta:
        model = Favorite
        fields = (
            "id",
            "hotel",
            "user",
            "hotel_id",
        )
        read_only_fields = ["user"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["user"]
