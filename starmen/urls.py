from django.urls import path

from .views import (index,
                    about,
										addpage,
										contact,
										login,
                    show_post,
                    page_not_found,)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
		path('addpage/', addpage, name='add_page'),
		path('contact/', contact, name='contact'),
		path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]

handler404 = page_not_found
