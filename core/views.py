from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    return render(request=request, template_name=template_name)
