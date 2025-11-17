"""
URL configuration for MultiApps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# from Firstapp import views as v1
# from SecondApp import views as v2

#or 

from Firstapp.views import display1
from SecondApp.views import display2


urlpatterns = [
    path("admin/", admin.site.urls),
    path("display1", display1),
    path("display2", display2),
]
