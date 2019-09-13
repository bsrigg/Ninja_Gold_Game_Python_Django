from django.urls import path
from . import views

urlpatterns=[
    path('resetme', views.resetme),
    path('', views.index),
    path('farm', views.farm),
    path('house', views.house),
    path('cave', views.cave),
    path('casino', views.casino),
]