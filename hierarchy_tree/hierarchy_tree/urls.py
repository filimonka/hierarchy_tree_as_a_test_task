from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('employee.urls', namespace='employee')),
    path('admin/', admin.site.urls),
]
