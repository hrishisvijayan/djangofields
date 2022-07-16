from django.urls import URLPattern, path

from . import views




print('this is app url')

urlpatterns = [
    path('', views.index, name='index'),
]