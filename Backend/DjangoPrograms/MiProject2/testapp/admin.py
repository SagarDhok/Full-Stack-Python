from django.contrib import admin
from testapp.models import *

# Register your models here.

from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)


class ProxyEmployee1Admin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']
class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']
admin.site.register(ProxyEmployee1,ProxyEmployee1Admin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)