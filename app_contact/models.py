from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:

        return f'{self.first_name} {self.last_name}'
    