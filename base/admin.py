from django.contrib import admin

# Register your models here.
from .models import Detect, Category


class DetectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'category', 'photo')
    list_display_links = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ("category",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Detect, DetectAdmin)
admin.site.register(Category, CategoryAdmin)
