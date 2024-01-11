from django.urls import reverse
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Starmen.Status.PUBLISHED)


class Starmen(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Еще редактируется'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        choices=Status.choices, default=Status.PUBLISHED)

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [models.Index(fields=['time_create'])]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
