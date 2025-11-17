from django.contrib import admin
from testapp.models import FilterMode

# Register your models here.

class FilterModeAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']
admin.site.register(FilterMode,FilterModeAdmin)