from django.contrib import admin

from .models import Barang, Jenis
from .models import Brand

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','jenis_id']
    search_fields = ['kodebrg','nama']
    list_filter = ('jenis_id',)
    list_per_page = 3

class dataBrand(admin.ModelAdmin):
    list_display = ['kodebrand', 'namaba', 'kategori', 'periode']
    search_fields = ['kodebrand', 'namaba']
    list_filter = ('kategori',)
    list_per_page = 3

admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)
admin.site.register(Brand,dataBrand)