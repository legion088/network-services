from django.contrib import admin
from django.urls import path, include
from account.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls',
                     namespace='account')),
    path('services/', include('services.urls',
                              namespace='services'))
]

handler404 = page_not_found
