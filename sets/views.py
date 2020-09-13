from django.shortcuts import render
from .models import Set
from django import http


def index(request):
    context = {'sets': Set.objects.all()}
    template_name = 'sets/index.html'
    return render(request, template_name, context)


def detail(request, set_id):
    try:
        set = Set.objects.get(id=set_id)
    except Set.DoesNotExist:
        raise http.Http404("Set doesn't exist")
    context = {'set': set}
    return render(request, 'sets/detail.html', context)
