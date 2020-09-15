from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField()
    cover_image1 = models.ImageField(null=True)
    cover_image2 = models.ImageField(null=True)
    designation = models.CharField(max_length=100, null=True)
    current_address1 = models.CharField(max_length=100, null=True)
    current_address2 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.firstname, self.user.lastname)




