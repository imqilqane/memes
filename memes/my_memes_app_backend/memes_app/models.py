from re import T
from django.db import models
from user.models import User
# Create your models here.


class Meme(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    icon_url = models.CharField(max_length=550)
    meme_value = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        try:
            return self.user.username
        except:
            return "memeObj"

    class Meta:
        ordering = ['added_at', ]
