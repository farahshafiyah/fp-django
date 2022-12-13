from django.db import models

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True) 
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return self.nama
        return "{} - {} - {}".format(self.kodebrg, self.nama, self.stok)

class Brand(models.Model):
    kodebrand=models.CharField(max_length=8)
    namaba=models.CharField(max_length=50)
    kategori=models.CharField(max_length=50)
    periode=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        # return self.nama
        return "{} - {} - {}".format(self.kodebrand, self.namaba, self.kategori)
