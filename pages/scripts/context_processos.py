from pages.models import Pages

def get_pages(request):
    pages  = Pages.objects.filter(visible = True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages':pages
    }