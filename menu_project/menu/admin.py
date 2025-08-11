from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    search_fields = ('title', 'menu_name', 'named_url', 'url')
    ordering = ('menu_name', 'order', 'id')
    list_editable = ('order',)
    autocomplete_fields = ('parent',)
    fieldsets = (
        (None, {
            'fields': ('menu_name', 'title', 'parent', 'order')
        }),
        ('Ссылки', {
            'fields': ('named_url', 'url'),
            'description': 'Можно указать либо named_url (рекомендуется), либо явный URL.'
        }),
    )