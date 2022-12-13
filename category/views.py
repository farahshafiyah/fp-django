from django.shortcuts import render

def category(request):
    title= "Category"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'category.html', konteks, {'navbar': 'category'})
    