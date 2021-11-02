from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('my_app/', include('my_app.urls')),
    path('admin/', admin.site.urls),
    
]
