from django.contrib import admin

from testapp.models import movies


class MovieAdmin(admin.ModelAdmin):
                list_display = ['rdate','moviename','hero','heroine','rating']

admin.site.register(movies,MovieAdmin)

