from django.urls import path

from .views import home, pricing

urlpatterns = [
    path('', home, name='home'),
    path('pricing/', pricing, name='pricing')
]
