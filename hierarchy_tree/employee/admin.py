from django.contrib import admin
from .models import Employee, Superior

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'position', 'get_salary')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Superior)