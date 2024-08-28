from django import template
from django import template
register = template.Library()

@register.filter(name='first_n_words')
def first_n_words(value, n):
    words = value.split()
    n = int(n)
    return ' '.join(words[:n])

@register.filter(name='rest_of_words')
def rest_of_words(value, n):
    words = value.split()
    n = int(n)
    return ' '.join(words[n:])


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)