from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models import Count


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    geolocation = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(max_length=255, upload_to="", null=True, blank=True)

    def __str__(self):
        return self.name

    def overall_rating(self):
        rev_rating = 0
        count = 0
        reviews = Review.objects.filter(hotel=self)
        favorites = Favorite.objects.filter(hotel=self).count()
        for review in reviews:
            rev_rating += review.rating
            count += 1
        try:
            # Favorites as counted as 5 star rating
            rating = (rev_rating + favorites * 5) / (count + favorites)
        except:
            rating = 0
        return rating


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "user",
            "hotel",
        )


class Review(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotel_reviews"
    )
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = (
            "user",
            "hotel",
        )

    def __str__(self):
        return " Review text: %s, Rating given: (%d)" % (self.description, self.rating)


class Like(models.Model):
    CHOICES = (("1", "Like"), ("2", "Dislike"))
    like_choice = models.CharField(max_length=7, choices=CHOICES)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
