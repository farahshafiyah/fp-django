from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, Brand
from django.contrib import messages


def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Add Data !")
            form = FormBarang()
            title = "Add Barang"
            konteks = {
            'form': form,
            'titlenya': title,
            }
        return render(request, 'tambah_barang.html', konteks)
    
    else:
        form = FormBarang()
        title = "Add Barang"
        konteks = {
            'form': form,
            'titlenya': title,
        }
    return render(request, 'tambah_barang.html', konteks)


def dashboard(request):
    title = "Dashboard"
    konteks = {
        'titlenya': title,
    }
    # return render(request, 'dashboard.html', konteks)
    return render(request, 'tampil_brg.html', konteks)


def Barang_View(request):
    barangs = Barang.objects.all()
    title = "Data Barang"
    konteks = {
        'barangs': barangs,
        'titlenya': title,
    }

    return render(request, 'tampil_brg.html', konteks)


def Brand_View(request):
    brands = Brand.objects.all()
    title = "Data Brand"
    konteks = {
        'brands': brands,
        'titlenya': title,
    }

    return render(request, 'tampil_brand.html', konteks)
