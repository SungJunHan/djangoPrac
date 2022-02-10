from django.urls import path
from .views import *

# from . import views




urlpatterns  = [
    path('/read', GetVideo.as_view()),
    # path('', views.Youtube),
]