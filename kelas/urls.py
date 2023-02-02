from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
# from dashboard.views import dashboard, tambah_barang, Barang_View, Brand_View
from dashboard.views import *
from category.views import category
from jenis.views import jenis


# def coba1(request):
#     return HttpResponse('Selamat Datang !')


def coba2(request):
    title = "Home"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'home.html', konteks)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba1),
    path('', coba2),
    path('category/', category),

    # barang (produk)
    path('barang/', Barang_View, name='view_barang'),
    path('addbrg/', tambah_barang),
    path('ubah/<int:id_barang>', ubah_brg, name='ubah_brg'),
    path('hapus/<int:id_barang>', hapus_brg, name='hapus_brg'),

    # brand (ambasador)
    path('brand/', Brand_View, name='view_brand'),
    path('addbrand/', tambah_brand),
    path('ubahh/<int:id_brand>', ubah_brand, name='ubah_brand'),
    path('hapuss/<int:id_brand>', hapus_brand, name='hapus_brand'),

    # jenis produk
    path('jenis/', Jenis_View),
    path('addjenis/', tambah_jenis),
    path('uubah/<int:id_jenis>', ubah_jenis, name='ubah_jenis'),
    path('hhapus/<int:id_jenis>', hapus_jenis, name='hapus_jenis'),
]
