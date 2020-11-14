from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Photo
from .forms import Add_image


# Create your views here.
def get_gallery(request):
    temp = loader.get_template('simplegallery\index.html')
    photos = Photo.objects.all()
    return HttpResponse(temp.render({"photos": photos}, request))


def get_form(request):
    if request.method == "POST":
        form = Add_image(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(1111111, request.POST, request.FILES["myfile"])
        # not_title = form.fields["title"]
        # not_image = form.fields["image"]
        # not_caption = form.fields["caption"]
        # return HttpResponse(f"<h2>{not_title}</h2> <img src='{not_image}'> <h3>{not_caption}</h3>")
        # but = Photo(title=not_title, image=not_image, captions=not_caption)
        # but.save()
    else:
        form = Add_image()
    return render(request, 'simplegallery/form.html', {"form": form})
