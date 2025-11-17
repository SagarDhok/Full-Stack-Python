"""
URL configuration for CbvProject project.

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
from django.urls import path
from testapp.views import Helloworld,TemplateCBV,TemplateCBV2,BookListView,BookListViewCustomized,BookDetailView,BookCreateView,BookUpdateView,BookDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Helloworld.as_view()),
    path('tc', TemplateCBV.as_view()),
   path('tc2/',TemplateCBV2.as_view()),

   path('list/', BookListView.as_view()) ,
   path('listc/', BookListViewCustomized.as_view(),name = 'listbook') ,

   path('<int:pk>',BookDetailView.as_view(),name = 'detail'),
   path('create/', BookCreateView.as_view()),
    path('update/<int:pk>',BookUpdateView.as_view()),
    path('delete/<int:pk>',BookDeleteView.as_view()),
]
