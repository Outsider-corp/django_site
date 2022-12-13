from django import template
from django.db.models import Count
from django.core.cache import cache

from news.models import Categories, News

register = template.Library()


@register.simple_tag(name="catsss")
def get_cat():
    return Categories.objects.all()


@register.inclusion_tag("news/list_categories.html")
def show_cats():
    # categories = Categories.objects.all()
    # categories = cache.get('category')
    # if not categories:
    #     categories = Categories.objects.filter(news__is_publ=1).annotate(cnt=Count('news')).filter(cnt__gt=0)
    #     cache.set("category", cats, 60)
    categories = Categories.objects.filter(news__is_publ=1).annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {"cats_list": categories}


@register.simple_tag()
def new_def():
    return News.objects.get(pk=1).image.url
