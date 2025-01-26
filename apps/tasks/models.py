from django.db import models
from autoslug import AutoSlugField


class Task(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ("Incomplete", "Incomplete"),
    )
    slug = AutoSlugField(populate_from='name')
    name = models.CharField()
    description = models.TextField()
    status = models.CharField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
