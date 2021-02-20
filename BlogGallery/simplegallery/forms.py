from django import forms
from .models import Photo


class Add_image(forms.ModelForm):
    class Meta():
        model = Photo
        fields = '__all__'


class Inf(forms.ModelForm):
    class Meta():
        model = Photo
        fields = '__all__'


class Bootswatch(forms.Form):
    themes = []