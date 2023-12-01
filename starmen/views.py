from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    return render(
        request, "starmen/index.html", {"menu": menu,
                                        "title": "Главная страница"}
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
