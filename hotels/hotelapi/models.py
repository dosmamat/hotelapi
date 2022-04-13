from django.db import models


class Hotel(models.Model):
    MOSCOW = 'MS'
    PITER = 'SP'
    CITIES_CHOICES=[
        (MOSCOW, 'Москва'),
        (PITER, 'Питер'),
    ]
    row_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=2, choices=CITIES_CHOICES, default=MOSCOW)
    image = models.ImageField(upload_to='hotels/images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    row_id = models.CharField(max_length=50, primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.row_id
