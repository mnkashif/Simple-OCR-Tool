from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image
import pytesseract
from PIL import Image as img
import os
from django.conf import settings
# Create your views here.


def gallery(request):
    images =  Image.objects.all()
    names = [os.path.splitext(i.image.name)[0] for i in images]
    images=zip(images,names)
    context = {'images':images}
    return render(request,'ocr/gallery.html',context)

def view_image(request,pk):
    photo = Image.objects.get(id=pk)
    c=0
    
    if request.method == 'POST':
        data = request.POST
        initial_path=photo.image.path
        new_name=""
        for i in range(len(data['image_name'])):
            if(data['image_name'][i]==' '):
                new_name+=str('_')
            else:
                new_name+=str(data['image_name'][i])
        final_path=str(settings.MEDIA_ROOT)+'/'+new_name+'.png'
        for path in Image.objects.all():
            if(final_path==path.image.path):
                c=1
        if c==0 :
            os.rename(initial_path,final_path);
            photo.image.name=new_name+'.png'
            photo.save()
        

        # return redirect('photo')
    name=os.path.splitext(photo.image.name)[0]
    im1 = img.open(photo.image.path)
    ocr = pytesseract.image_to_string(im1,lang='eng', config='--psm ' +str(6))
    
    # ocr = 'yo'
    context = {'photo':photo,'ocr':ocr,'name':name,'c':c}
    return render(request,'ocr/view_image.html',context)


def add_images(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        print(len(images))
        for i in images:
            photo = Image.objects.create(image=i)   

        return redirect('gallery')
    return render(request,'ocr/add_image.html')
