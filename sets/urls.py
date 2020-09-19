from django.urls import path
from .views import index, detail, SetListView

urlpatterns = [
    path('sets/', index, name='sets-list'),
    path('class/sets/', SetListView.as_view(), name='sets-list-class'),
    path('sets/<int:set_id>/', detail, name='sets-detail')
]
