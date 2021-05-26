from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    return render(request=request, template_name=template_name)


def pricing(request):
    template_name = 'pricing.html'
    return render(request=request, template_name=template_name)
