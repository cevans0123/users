from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    age = models.IntegerField(default=17)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField