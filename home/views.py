from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
# Create your views here.


def upload(request):
    if request.method =='POST':
        form = ImageForm(data=request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'home.html',{'obj':obj})
    else:
        form=ImageForm()
    
    return  render(request,'home.html',{'form':form})