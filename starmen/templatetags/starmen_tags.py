from django import template
from starmen.models import Category, TagPost

import starmen.views as views

register = template.Library()


@register.inclusion_tag('starmen/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected_id}


@register.inclusion_tag('starmen/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}
