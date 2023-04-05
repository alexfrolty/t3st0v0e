from django.contrib import admin
from treemenu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'named_url')
    list_filter = ('parent',)
    search_fields = ('name', 'url', 'named_url')


