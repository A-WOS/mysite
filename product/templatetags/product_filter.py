from django import template

register = template.Library()


@register.filter
def sub2(value, arg):
    return value - arg

