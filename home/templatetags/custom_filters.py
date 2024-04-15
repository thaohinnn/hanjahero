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
    """Sums an attribute from a dictionary of dictionaries."""
    return sum(item.get(arg, 0) for item in value.values())


@register.filter(name='get_format_description')
def get_format_description(format_list, key):
    return next((item.get(key, None) for item in format_list if key in item), None)


@register.filter(name='convert_exam_name')
def convert_exam_name(value):
    exam_names = {1: '기출 35회',
    2: '기출 36회',
    3: '기출 37회',
    4: '기출 41회',
    5: '기출 47회',
    6: '기출 52회',
    7: '기출 60회',
    8: '기출 64회'
                  }
    return exam_names.get(value, "Unknown Exam")


@register.filter(name='convert_skill_name')
def convert_skill_name(value):
    skill_names = {1: '듣기', 2: '쓰기', 3: '읽기'}

    return skill_names.get(value, "Unknown Skill")
