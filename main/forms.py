from django import forms
from .models import *

class TalabaForm(forms.Form):
    ism = forms.CharField(max_length=255, min_length=3)
    guruh = forms.CharField(max_length=255, min_length=1)
    kurs = forms.IntegerField(min_value=1, max_value=5)
    kitob_soni = forms.IntegerField(min_value=0)

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = "__all__"