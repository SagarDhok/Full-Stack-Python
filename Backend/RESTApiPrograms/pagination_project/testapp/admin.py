from django.contrib import admin

# Register your models here.

from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal']
admin.site.register(Employee,EmployeeAdmin)