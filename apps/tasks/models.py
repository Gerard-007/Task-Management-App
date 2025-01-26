from django.db import models
from autoslug import AutoSlugField

from core import settings


class Task(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ("Incomplete", "Incomplete"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name')
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
