from django.shortcuts import render

# Create your views here.

def home_page_view(request):
                # return render(request,"testapp\index.html")        
                return render(request, "testapp/index.html")        