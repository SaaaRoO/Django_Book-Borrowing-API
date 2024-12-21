from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('interfaces.urls')),
]
from django.contrib import admin
from django.urls import path, include
from interfaces.views import root_view  # Import the root view

urlpatterns = [
    path('', root_view, name='root'),  # Add root path
    path('admin/', admin.site.urls),
    path('api/', include('interfaces.urls')),  # Include API URLs
]
