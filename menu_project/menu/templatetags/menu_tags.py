from django import template
from django.urls import resolve
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/index.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if not request:
        current_url = '/'
    else:
        current_url = request.path_info

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').prefetch_related('children').order_by('order')

    active_item = None
    for item in menu_items:
        if item.get_url() == current_url:
            active_item = item
            break

    expanded_items = set()
    if active_item:
        current = active_item
        while current:
            expanded_items.add(current.id)
            current = current.parent
        for child in active_item.children.all():
            expanded_items.add(child.id)

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent_id == (parent.id if parent else None):
                children = build_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_expanded': item.id in expanded_items
                })
        return tree

    menu_tree = build_tree(menu_items)

    return {
        'menu_tree': menu_tree,
        'current_url': current_url
    }