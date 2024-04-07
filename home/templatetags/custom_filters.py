# custom_filters.py

from django import template

register = template.Library()


@register.filter(name='is_integer')
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
