from django.forms import ModelForm
from dashboard.models import Barang, Brand, Jenis
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }


class FormBrand(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

        widgets = {
            'kodebrand': forms.TextInput({'class': 'form-control'}),
            'namaba': forms.TextInput({'class': 'form-control'}),
            'jenis_id': forms.Select({'class': 'form-control'}),
            'periode': forms.NumberInput({'class': 'form-control'}),
        }


class FormJenis(ModelForm):
    class Meta:
        model = Jenis
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'ket': forms.TextInput({'class': 'form-control'}),
        }
