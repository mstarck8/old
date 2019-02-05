from django.db import models
from django.utils import timezone


class ArtikelPost(models.Model):
    überschrift = models.TextField(max_length=50)
    inhalt = models.TextField(max_length=10000)
    created_at = models.DateTimeField(max_length=10, default=timezone.now)
