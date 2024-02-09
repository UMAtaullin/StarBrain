from django import forms

from starmen.models import Category, Company


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(
        max_length=255, label='URL')
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        required=False,
        label='Контент')
    is_published = forms.BooleanField(
        required=False,
        label='Статус',
        initial=True)
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Категория не выбрана')
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        required=False,
        label='Компания',
        empty_label='Нет компании')
