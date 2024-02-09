from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from starmen.forms import AddPostForm

from starmen.models import Category, Starmen, TagPost

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


def index(request):
    posts = Starmen.published.all().select_related('cat')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(
        request,
        'starmen/index.html',
        context=data
    )


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
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


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Starmen.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка при добавлении поста')
    else:
        form = AddPostForm()

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


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Starmen.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'starmen/index.html', data)


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
