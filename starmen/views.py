from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from starmen.forms import AddPostForm, UploadFileForm

from starmen.models import Category, Starmen, TagPost, UploadFiles

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]

cats_db = [
    {'id': 1, 'name': 'Ученые'},
    {'id': 2, 'name': 'Предприниматели'},
    {'id': 3, 'name': 'Политики'},
]


# def index(request):
#     posts = Starmen.published.all().select_related('cat')
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0
#     }
#     return render(
#         request,
#         'starmen/index.html',
#         context=data
#     )


class StarmenHome(ListView):
    # model = Starmen
    template_name = 'starmen/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0
    }

    def get_queryset(self):
        return Starmen.published.all().select_related('cat')


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            # cleaned_data - это словарь, который содержит данные из формы,
            # прошедшие все валидации, определенные в форме
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'menu': menu,
        'form': form
    }
    return render(request, 'starmen/about.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Starmen, slug=post_slug)
    data = {
        'title': 'post.title',
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'starmen/post.html', data)


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # # print(form.cleaned_data)
#             # try:
#             #     Starmen.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка при добавлении поста')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     data = {
#         'title': 'Добавление статьи',
#         'menu': menu,
#         'form': form,
#     }
#     return render(request, 'starmen/addpage.html', data)


class AddPage(View):

    def get(self, request):
        form = AddPostForm()
        data = {
            'title': 'Добавление статьи',
            'menu': menu,
            'form': form,
        }
        return render(request, 'starmen/addpage.html', data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'title': 'Добавление статьи',
            'menu': menu,
            'form': form,
        }
        return render(request, 'starmen/addpage.html', data)


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Starmen.published.filter(cat_id=category.pk).select_related('cat')
#     data = {
#         'title': f'Рубрика: {category.name}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': category.pk
#     }
#     return render(request, 'starmen/index.html', data)


class StarmenCategory(ListView):
    template_name = 'starmen/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Starmen.published.filter(
            cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(
        is_published=Starmen.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }
    return render(request, 'starmen/index.html', data)
