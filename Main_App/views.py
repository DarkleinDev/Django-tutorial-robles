from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Main_app/index.html', {
        'titulo':'Hello Word',
    })
def abaut(request):
    return render(request, 'Main_app/abaut.html',{
        'titulo':'abaut',
    })