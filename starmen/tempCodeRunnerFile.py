class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Starmen.Status.PUBLISHED)