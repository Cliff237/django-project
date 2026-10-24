from django import template
from django.db.models import Avg
from django.utils.http import urlencode

register = template.Library()

@register.filter
def avg(value, arg):
    """
    Returns the average of the given attribute in a list of objects.
    Usage: {{ queryset|avg:"field_name" }}
    """
    if not value:
        return 0
    total = sum(getattr(obj, arg) for obj in value)
    return total / len(value)


@register.filter
def floor(value):
    """
    Returns the floor of a number.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


@register.filter
def subtract(value, arg):
    """
    Subtracts the arg from the value.
    """
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    """
    Returns the URL-encoded querystring for the current page,
    updating the params with the given kwargs.

    Usage: {% query_transform page=2 %} or {% query_transform page=1 q='search' %}
    """
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            query[k] = v
        else:
            query.pop(k, 0)
    return query.urlencode()