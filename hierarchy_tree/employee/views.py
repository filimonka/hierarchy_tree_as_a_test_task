from django.shortcuts import render
from .models import Employee


def show_tree(requests):
    template = 'tree.html'
    employee = Employee.objects.all()
    context = {
        'all_stuff': employee, 
    }
    return render(requests, template, context)
