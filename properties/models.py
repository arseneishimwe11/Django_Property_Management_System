from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)  # e.g. Apartment, House
    address = models.CharField(max_length=255)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    # amenities = models.TextField()
    # size_in_sqft = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.name
