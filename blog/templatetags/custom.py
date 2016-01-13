from django.template.base import Library
register = Library()


@register.filter(is_safe=True)
def get_range(value):
    return xrange(value)