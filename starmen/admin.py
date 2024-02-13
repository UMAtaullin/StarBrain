from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from .models import Starmen, Category


class CompanyFilter(admin.SimpleListFilter):
    title = 'Семейное положение'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'В браке'),
            ('single', 'В браке не состоит'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(company__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(company__isnull=True)


@admin.register(Starmen)  # admin.site.register(Starmen, StarmenAdmin)
class StarmenAdmin(admin.ModelAdmin):
    # поля, которые будут отображаться в форме редактирования статьи.
    fields = ('title',  'slug', 'content', 'photo', 'post_photo', 'cat', 'company', 'tags')
    # будут отображаться в форме но не редактироваться
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}  # автозаполнение slug на основе title.
    filter_horizontal = ['tags']
    list_display = ('id',   # список отображаемых полей модели.
                    'title',
                    'post_photo',
                    'time_create',
                    'is_published',
                    'cat',)
    list_display_links = ('id',     # список кликабельных полей модели.
                          'title')
    ordering = ['time_create', 'title']
    list_editable = ('is_published', 'cat')     # список редактируемых полей.
    list_per_page = 5   # число отображаемых записей на странице в админке.
    # список пользовательских действий.
    actions = ['set_published', 'set_draft']
    # список полей, по которым осуществляется поиск.
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [CompanyFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Изображение', ordering='content')
    def post_photo(self, starmen: Starmen):
        if starmen.photo:
            return mark_safe(f'<img src="{starmen.photo.url}" width=50>')
        return 'Без фото'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Starmen.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записи.')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Starmen.Status.DRAFT)
        self.message_user(request,
                          f'{count} записей cнято с публикаций!', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
