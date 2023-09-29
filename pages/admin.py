from django.contrib import admin
from .models import Pages
# Register your models here.

admin.site.register(Pages)

#configuracion del panel de la app pages
title = "Proyecto de Django"
subtitle = "Tutorial Victor Robles"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle