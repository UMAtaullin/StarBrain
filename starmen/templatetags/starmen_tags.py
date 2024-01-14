from django import template
from starmen.models import Category

import starmen.views as views

register = template.Library()


@register.inclusion_tag('starmen/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected_id}
