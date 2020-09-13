from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    return render(request=request, template_name=template_name)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('', include('sets.urls'))
]
