from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Photo, Choosen_One
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import Add_image


# Create your views here.
# def get_gallery(request):
#     temp = loader.get_template('simplegallery/index.html')
#     photos = Photo.objects.all()
#     theme = Choosen_One.objects.all()[0].theme
#     return HttpResponse(temp.render({"photos": photos, "theme": theme}, request))
#

def get_form(request):
    theme = Choosen_One.objects.all()[0].theme
    if request.method == "POST":
        form = Add_image(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(1111111, request.POST, request.FILES["myfile"])
    else:
        form = Add_image()
    return render(request, 'simplegallery/form.html', {"form": form, "theme": theme})


def get_theme(request, theme):
    t = Choosen_One.objects.all()[0]
    t.theme = theme
    t.save()
    return HttpResponse()


def auth(request):
    theme = Choosen_One.objects.all()[0].theme
    print(request.user, request.session)
    if request.method == 'POST':
        login = request.POST["login"]
        password = request.POST["password"]
        user = authenticate(username=login, password=password)
        if user is None:
            temp = loader.get_template('simplegallery/auth.html')
            context = {"login_error": True, "theme": theme}
            return HttpResponse(temp.render(context, request))
        else:
            return redirect(f'../main_page/{user.id}')
    else:
        temp = loader.get_template('simplegallery/auth.html')
        context = {"password_error": False, "theme": theme}
        return HttpResponse(temp.render(context, request))


def main_page(request, user=False):
    print(request.user, request.session.keys(), request.session.values())
    temp = loader.get_template('simplegallery/index.html')
    photos = Photo.objects.all()
    theme = Choosen_One.objects.all()[0].theme
    if user:
        user = User.objects.get(id=user)
    context = {"user": user, "photos": photos, "theme": theme}
    return HttpResponse(temp.render(context, request))
