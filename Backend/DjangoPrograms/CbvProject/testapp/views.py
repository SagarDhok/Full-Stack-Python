from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse


# Create your views here.


class Helloworld(View):
                def get(self,request):
                         return HttpResponse('<h1>This response is from class based view</h1>')


class TemplateCBV(TemplateView):
        template_name = 'testapp/result.html'

class TemplateCBV2(TemplateView):
        template_name = 'testapp/result2.html'
        def get_context_data(self, **kwargs):
                context =  super().get_context_data(**kwargs)
                context['name'] = 'Sunny'
                context['marks'] = 98
                context['subject'] = 'Python'
                return context


from testapp.models import Book
class BookListView(ListView):
    model = Book

#! how to configure our own tempate file and context object:
#! -----------------------------------------------------------------------------------------
#! By using template_name & context_object_name variables


class BookListViewCustomized(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'



class BookDetailView(DetailView):
        model = Book

class BookCreateView(CreateView):
        model = Book
        fields = ('title','author','pages','price')

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbook')
