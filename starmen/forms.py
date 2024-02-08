from django import forms

from starmen.models import Category, Company


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length= 255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(), required=False)
