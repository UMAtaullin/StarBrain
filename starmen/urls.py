from django.urls import path

from .views import (index,
                    about,
                    categories,
                    categories_by_slug,
                    page_not_found,)

urlpatterns = [
	path('', index, name='home'),
	path('about/', about, name='about'),
	path('cats/<int:cat_id>/', categories, name='cats_id'),
	path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
]

handler404 = page_not_found
