import datetime

from django import template

register = template.Library()


@register.filter
def format_date(value):
    now = datetime.datetime.now()
    value = datetime.datetime.fromtimestamp(value)
    res = value - now
    duration_in_s = res.total_seconds()
    if duration_in_s < -86400:
        return value
    elif -86400 < duration_in_s < -600:
        return f'{abs(round(duration_in_s / 60 / 60))} часов назад'
    elif -600 < duration_in_s < 0:
        return f'только что'
    return value


# необходимо добавить фильтр для поля `score`
@register.filter
def score(value):
    if value < -5:
        return f'все плохо'
    elif -5 <= value <= 5:
        return f'нейтрально'
    elif value > 5:
        return f'хорошо'


@register.filter
def format_num_comments(value):
    if value <= 0:
        return f'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    elif value > 50:
        return f'50+'


@register.filter
def format_selftext(value, count):
    lst = value.split()

    first_words = lst[0:count]
    last_words = lst[-count:]

    str_first_words = ' '.join(first_words)
    str_last_words = ' '.join(last_words)

    res = f'{str_first_words}...{str_last_words}'
    return res
