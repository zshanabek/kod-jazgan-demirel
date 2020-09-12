from django.shortcuts import render
from .models import Set


def index(request):
    context = {'sets': Set.objects.all()}
    template_name = 'sets/index.html'
    return render(request=request, template_name=template_name, context=context)
