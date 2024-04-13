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


@register.filter
def safe_get(dictionary, key):
    if dictionary:
        return dictionary.get(key)
    return None


@register.filter(name='sum_attribute')
def sum_attribute(value, arg):
    """Sums the value of a key specified by 'arg' across all dictionaries in the 'value' dictionary."""
    return sum(sub_dict.get(arg, 0) for sub_dict in value.values())


@register.filter(name='get_format_description')
def get_format_description(format_list, key):
    return next((item.get(key, None) for item in format_list if key in item), None)
