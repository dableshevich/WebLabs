from django.urls import path

from . import views

urlpatterns = [
    path('set-info', views.set_info, name='set-info'),
    path('get-info', views.get_info, name='get-info')
]
