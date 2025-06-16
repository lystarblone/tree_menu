from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    search_fields = ('title', 'menu_name')
    list_editable = ('order',)
    autocomplete_fields = ('parent',) if 'autocomplete_fields' in dir(admin.ModelAdmin) else ()

    fieldsets = (
        (None, {
            'fields': ('menu_name', 'title', 'url', 'named_url', 'parent', 'order')
        }),
    )