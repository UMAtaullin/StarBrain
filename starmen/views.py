from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return HttpResponse("Страница приложения starmen.")


def categories(request):
	return HttpResponse("<h1>Статьи по категориям</h1>")
