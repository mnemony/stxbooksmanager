
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('library_bk.urls')),
    path('admin/', admin.site.urls),
    
]
