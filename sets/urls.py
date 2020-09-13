from django.urls import path
from .views import index, detail

urlpatterns = [
    path('sets/', index, name='sets-list'),
    path('sets/<int:set_id>/', detail, name='sets-detail')
]
