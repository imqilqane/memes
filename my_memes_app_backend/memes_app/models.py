from django.db import models
# Create your models here.


class Meme(models.Model):
    icon_url = models.CharField(max_length=550)
    meme_value = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ['added_at', ]
