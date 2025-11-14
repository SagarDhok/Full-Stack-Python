"""
URL configuration for AuthProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from testapp.views import home_view,java_page_view,python_page_view,aptitude_page_view,logout_view,Signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('java/', java_page_view),
    path('python/', python_page_view),
    path('apptitude/',aptitude_page_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',logout_view),
    path('signup/',Signup_view),
# *    Problem-2:
# ----------------
#* TemplateDoesNotExist at /accounts/login/
#* registration/login.html
# *-->Create a folder under 'templates' with the name of 'registration' and create a file login.html
]
