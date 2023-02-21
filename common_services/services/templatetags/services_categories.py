from django import template
from services.views import Categories
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_categories():
    return Categories.objects.annotate(
        count=Count('services_categories')).\
        filter(count__gt=0)
