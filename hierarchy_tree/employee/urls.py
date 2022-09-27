from django.urls import path
from .views import show_tree

app_name = 'employee'

urlpatterns = [
    path('', show_tree, name='employee_list')
]