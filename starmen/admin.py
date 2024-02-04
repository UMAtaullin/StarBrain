from django.contrib import admin, messages
from .models import Starmen, Category


@admin.register(Starmen)  # admin.site.register(Starmen, StarmenAdmin)
class StarmenAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'time_create',
                    'is_published',
                    'cat',
                    'brief_info',)
    list_display_links = ('id',
                          'title')
    ordering = ['time_create', 'title']
    list_editable = ('is_published', 'cat')
    list_per_page = 5
    actions = ['set_published', 'set_draft']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, starmen: Starmen):
        return f'В описании {len(starmen.content)} символов.'

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
