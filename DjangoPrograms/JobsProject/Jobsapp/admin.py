from django.contrib import admin
from Jobsapp.models import Hydjobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
                list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Hydjobs,HydJobsAdmin)
