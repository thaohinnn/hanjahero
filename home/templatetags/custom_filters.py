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


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_attribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    return None
