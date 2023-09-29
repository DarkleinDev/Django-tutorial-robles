from django.contrib import admin
from .models import Category, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'upgrate_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'upgrate_at')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
            
        obj.save()
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)