from django.db import models
from django.contrib.auth.models import User
 
class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    Key_name = models.CharField(max_length=100)

    provider_url = models.URLField()
    secret_key =  models.CharField(max_length=100)
    access_token = models.CharField(max_length=255)
    is_connected = models.BooleanField(default=False)  # New field
 
    def __str__(self):
        return self.provider_name