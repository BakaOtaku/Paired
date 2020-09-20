from django.shortcuts import render


from django.http import request,HttpResponse

from .models import Pic
# Create your views here.


def home(request):
    print("hello world")
    model=Pic.objects.all()
   
    context={
        "gif":model
        }

    return render(request,'index.html',context)
