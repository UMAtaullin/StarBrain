from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}]

data_db = [
    {'id': 1, 'title': 'Альберт Эйнштейн', 'content': '''<h1>Альберт Эйнштейн</h1> американский, немецкий и швейцарский физик-теоретик и общественный деятель-гуманист, один из основателей современной теоретической физики. Лауреат Нобелевской премии по физике 1921 года. Его теория относительности изменила основания физики, заменив классическую механику и закон всемирного тяготения Ньютона.''',
     'is_published': True},
    {'id': 2, 'title': 'Генри Форд',
        'content': 'Биография Генри Форд', 'is_published': False},
    {'id': 3, 'title': 'Махатма Ганди',
        'content': 'Биография Махатма Ганди', 'is_published': True},
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


def show_post(request, post_id):
    return HttpResponse("<h1>Отображение статьи с id = {post_id}</h1>")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
