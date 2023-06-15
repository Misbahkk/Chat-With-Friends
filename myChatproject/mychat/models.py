from django.db import models
from django.contrib.auth.models import User


# Add all models in admin.py file


# this model for user profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img', blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name='friend_profiles')

    def __str__(self):
        return self.name

# every friend have 1 profile


class Friend(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.profile.name

# friend message with user


class ChatMessage(models.Model):
    body = models.TextField()
    mxg_sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='mxg_sender')
    mxg_reciver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='mxg_reciver')
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body
