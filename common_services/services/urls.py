from django.urls import path
from .views import *

app_name = 'services'
urlpatterns = [
    path('', load_home, name='home'),
    path('<slug:slug>/', get_services, name='categories'),
]
