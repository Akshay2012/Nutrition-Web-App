
from django import template
register=template.Library()



@register.filter
def byindex(indexable, i):
    return indexable[i]