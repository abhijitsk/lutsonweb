from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
# Create your views here.

from .applyLuts import ApplyLuts

def upload(request):
    if request.method =='POST':
        form = ImageForm(data=request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # check the code
            asd =ApplyLuts(obj.image.url[1:])
            output =asd.ShowImages()
            return render(request,'home.html',{'obj':obj,'output':output})
    else:
        form=ImageForm()
        
    return  render(request,'home.html',{'form':form})