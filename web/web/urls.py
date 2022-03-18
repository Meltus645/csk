from django.contrib import admin
from django.urls import path, include

urlpatterns:list = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
