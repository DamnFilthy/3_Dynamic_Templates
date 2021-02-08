from django import template

register = template.Library()


@register.filter()
def cuto(value: str) -> str:
    return value.replace('o', '')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def make_float(value):
    try:
        result = float(value)
    except ValueError:
        result = value
    return result


