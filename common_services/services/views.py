from django.shortcuts import render, redirect, \
    get_list_or_404
from django.db.models import Count
from .models import *


def load_home(request):
    if not request.user.is_authenticated:
        return redirect('account:login')

    cats = Categories.objects.annotate(count=Count('services_categories')). \
        filter(count__gt=0).order_by('-count')
    context = {'active': True,
               'title': 'Главная страница',
               'cats': cats}
    return render(request,
                  'services/index.html',
                  context)


def get_services(request, slug):
    if not request.user.is_authenticated:
        return redirect('account:login')

    services = get_list_or_404(Services, categories_fk__slug=slug)
    rooms = Services.objects.filter(categories_fk__slug=slug). \
        values_list('room_fk__room', flat=True).distinct() \
        .order_by('room_fk__room')
    title = Categories.objects.get(slug=slug).name

    context = {'services': services,
               'rooms': rooms,
               'slug': slug,
               'title': title}

    return render(request,
                  'services/hard-services-categories.html',
                  context)
