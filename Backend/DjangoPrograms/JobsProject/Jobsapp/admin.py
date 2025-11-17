from django.contrib import admin
from Jobsapp.models import Hydjobs,Punejobs,Bangjobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
                list_display = ['date','company','title','eligibility','address','email','phonenumber']
class PunejobsAdmin(admin.ModelAdmin):
                list_display = ['date','company','title','eligibility','address','email','phonenumber']
class BangJobsAdmin(admin.ModelAdmin):
                list_display = ['date','company','title','eligibility','address','email','phonenumber']



admin.site.register(Hydjobs, HydJobsAdmin)
admin.site.register(Punejobs, PunejobsAdmin)
admin.site.register(Bangjobs, BangJobsAdmin)