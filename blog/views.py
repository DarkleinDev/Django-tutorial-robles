from django.shortcuts import render

# Create your views here.
def articles_list(request):
    return render(request,'articles/list.html', {
        'title': 'Articulos'
    })