from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('projects.urls')),
    path('admin/', admin.site.urls),
]
