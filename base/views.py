from distutils.command.upload import upload
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import PhotoGallery
from django.http import HttpResponse, JsonResponse
import os
import glob
import The_AccIO_Cloud.settings as settings
from PIL import Image

class MainView(TemplateView):
    template_name='drop/main.html'
    
def multiple_upload(request):
    if request.method =='POST':
        file_data=request.FILES.get('file')
        PhotoGallery.objects.create(upload=file_data)
    path = settings.MEDIA_ROOT
    searchfile = path + "\\images\\"
    img_list=list(filter(os.path.isfile, glob.glob(searchfile + "*")))
    img_list.sort(key=lambda x: os.path.getmtime(x))
    print(img_list)
    img_list.reverse()
    print(img_list)
    for im in img_list:
        a=im.split("\\")
        print(a)
        foo = Image.open(im)
        foo.save(path + "/compressed/"+a[-1],optimize=True,quality=30)
    imname=[]
    for ima in img_list:
        b=ima.split("\\")
        imname.append(b[-1])
    path = settings.MEDIA_ROOT
    img_list2 = os.listdir(path + "/compressed/")
    context = {"images": imname}
    return render (request, 'drop/gallery.html', context)
def delete_image(request, pk):
    if request.method =='POST':
        file=PhotoGallery.delete.get(pk.pk)
        file.delete()
    return redirect('gallery')