from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
     msg = "<h1>MY NAME IS ANTHONY GUNJLAIWISH</h1>"
     return HttpResponse(msg)