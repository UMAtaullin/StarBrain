from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1,
     'title': 'Анджелина Джоли',
     'content': 'Биография Анджелины Джоли',
     'is_published': True},

    {'id': 2,
     'title': 'Марго Робби',
     'content': 'Биография Марго Робби',
     'is_published': False},

    {'id': 3,
     'title': 'Джулия Робертс',
     'content': 'Биография Джулии Робертс',
     'is_published': True},
]


def index(request):
    return render(
        request,
        "starmen/index.html",
        {"menu": menu,
         "title": "Главная страница",
         "post": data_db},
    )


def about(request):
    return render(request, "starmen/about.html", {"menu": menu,
                                                  "title": "О сайте"})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}<p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}<p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
