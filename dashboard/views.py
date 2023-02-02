from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, FormBrand, FormJenis
from dashboard.models import Barang, Brand, Jenis
from django.contrib import messages

# Dashboard
def dashboard(request):
    title = "Dashboard"
    konteks = {
        'titlenya': title,
    }
    # return render(request, 'dashboard.html', konteks)
    return render(request, 'tampil_brg.html', konteks)


# Barang (produk)
def Barang_View(request):
    barangs = Barang.objects.all()
    title = "Data Barang"
    konteks = {
        'barangs': barangs,
        'titlenya': title,
    }

    return render(request, 'tampil_brg.html', konteks)


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


def ubah_brg(request, id_barang):
    barangs = Barang.objects.get(id=id_barang)
    if request.POST:
        form = FormBarang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Update Data !")
            return redirect('ubah_brg', id_barang=id_barang)

    else:
        form = FormBarang(instance=barangs)
        title = "Ubah Barang"
        konteks = {
            'form': form,
            'barangs': barangs,
            'titlenya' : title,
        }

    return render(request, 'ubah_brg.html', konteks)


def hapus_brg(request, id_barang):
    barangs = Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Deleted !")
    return redirect('/barang')


# Brand (ambasador)
def Brand_View(request):
    brands = Brand.objects.all()
    title = "Data Brand"
    konteks = {
        'brands': brands,
        'titlenya': title,
    }

    return render(request, 'tampil_brand.html', konteks)


def tambah_brand(request):
    if request.POST:
        form = FormBrand(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Add Data !")
            form = FormBrand()
            title = "Add Brand"
            konteks = {
                'form': form,
                'titlenya': title,
            }
        return render(request, 'tambah_brand.html', konteks)

    else:
        form = FormBrand()
        title = "Add Brand"
        konteks = {
            'form': form,
            'titlenya': title,
        }
    return render(request, 'tambah_brand.html', konteks)

def ubah_brand(request, id_brand):
    brands = Brand.objects.get(id=id_brand)
    if request.POST:
        form = FormBrand(request.POST, instance=brands)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Update Data !")
            return redirect('ubah_brand', id_brand=id_brand)

    else:
        form = FormBrand(instance=brands)
        title = "Ubah BA"
        konteks = {
            'form': form,
            'brands': brands,   
            'titlenya' : title,
        }

    return render(request, 'ubah_brand.html', konteks)


def hapus_brand(request, id_brand):
    brands = Brand.objects.filter(id=id_brand)
    brands.delete()
    messages.success(request, "Deleted !")
    return redirect('/brand')


# Jenis (jenis produk)
def Jenis_View(request):
    jeniss = Jenis.objects.all()
    title = "Data Jenis"
    konteks = {
        'jeniss': jeniss,
        'titlenya': title,
    }

    return render(request, 'tampil_jenis.html', konteks)


def tambah_jenis(request):
    if request.POST:
        form = FormJenis(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Add Data !")
            form = FormJenis()
            title = "Add Jenis"
            konteks = {
                'form': form,
                'titlenya': title,
            }
        return render(request, 'tambah_jenis.html', konteks)

    else:
        form = FormJenis()
        title = "Add Jenis"
        konteks = {
            'form': form,
            'titlenya': title,
        }
    return render(request, 'tambah_jenis.html', konteks)


def ubah_jenis(request, id_jenis):
    jeniss = Jenis.objects.get(id=id_jenis)
    if request.POST:
        form = FormJenis(request.POST, instance=jeniss)
        if form.is_valid():
            form.save()
            messages.success(request, "Success Update Data !")
            return redirect('ubah_jenis', id_jenis=id_jenis)

    else:
        form = FormJenis(instance=jeniss)
        title = "Ubah Jenis"
        konteks = {
            'form': form,
            'jeniss': jeniss,
            'titlenya' : title,
        }

    return render(request, 'ubah_jenis.html', konteks)


def hapus_jenis(request, id_jenis):
    jeniss = Jenis.objects.filter(id=id_jenis)
    jeniss.delete()
    messages.success(request, "Deleted !")
    return redirect('/jenis')
