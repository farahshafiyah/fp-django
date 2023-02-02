from django.shortcuts import render

def jenis(request):
    title = "Jenis"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'tampil_jenis.html', konteks)

