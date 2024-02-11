from django import forms

from starmen.models import Category, Company, Starmen


class AddPostForm(forms.ModelForm):
    """Форма для добавление новой записи."""

    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Категория не выбрана')
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        required=False,
        label='Компания',
        empty_label='Нет компании')

    class Meta:
        model = Starmen     # Описывает взаимосвязь формы с моделью.
        fields = ('title', 'slug', 'content',
                  'is_published', 'cat', 'company', 'tags',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        # labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise forms.ValidationError('Длина превышает 50 символов')
        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')
