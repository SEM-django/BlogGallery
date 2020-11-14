from django import forms
from .models import Photo


class Add_image(forms.ModelForm):
    # title = forms.CharField(label="Name")
    # image = forms.ImageField()
    # caption = forms.CharField(label="Sign")
    class Meta():
        model = Photo
        fields = "__all__"


class Bootswatch(forms.Form):
    themes = []