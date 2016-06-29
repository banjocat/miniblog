from django import template


register = template.Library()

@register.filter(name='nametohref')
def name_to_href(value):
    return value.replace(' ', '-')
