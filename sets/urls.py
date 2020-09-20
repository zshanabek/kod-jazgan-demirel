from django.urls import path
from .views import SetListView, SetDetailView

urlpatterns = [
    path('sets', SetListView.as_view(), name='sets-list'),
    path('sets/<int:pk>', SetDetailView.as_view(), name='sets-detail')
]
