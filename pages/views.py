from django.shortcuts import render
from .models import Pages
# Create your views here.
def page(request, slug):
    page = Pages.objects.get(slug = slug)
    return render(request, "pages/page.html",{
        "page" : page
    })