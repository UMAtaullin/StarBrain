from django.urls import reverse
from django.db import models
# from django.template.defaultfilters import slugify


def translit_to_eng(s: str):
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Starmen.Status.PUBLISHED)


class Starmen(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Еще редактируется'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/',
                              default=None, blank=True, null=True,
                              verbose_name='Фото')
    content = models.TextField(blank=True,
                               verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name='Время изменения')
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name="Статус")
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            related_name='posts',
                            verbose_name='Категории')
    tags = models.ManyToManyField('TagPost',
                                  blank=True,
                                  related_name='tags',
                                  verbose_name='Теги')
    company = models.OneToOneField('Company',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='company',
                                   verbose_name='Компания')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Известные люди'
        verbose_name_plural = 'Известные люди'
        ordering = ['-time_create']
        indexes = [models.Index(fields=['time_create'])]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translit_to_eng(self.title))
    #     super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=64,
                            db_index=True,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Company(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    s_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    """Модель таблицы в которой храняться ссылки на загруженные файлы."""
    file = models.FileField(upload_to='uploads')
