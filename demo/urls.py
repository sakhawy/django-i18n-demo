from django.urls import path

from demo import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
