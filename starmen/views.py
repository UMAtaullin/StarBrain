from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from starmen.models import Starmen

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
    posts = Starmen.published.all()
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
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': Starmen.published.all(),
        'cat_selected': cat_id
    }
    return render(request, 'starmen/index.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
