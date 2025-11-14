from django.shortcuts import render
from testapp.models import FilterMode

# Create your views here.


def data_view(request):
                records = FilterMode.objects.all()

                return render(request,'testapp/index.html',{"records":records})