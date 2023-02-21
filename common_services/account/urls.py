from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('comm-services/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
