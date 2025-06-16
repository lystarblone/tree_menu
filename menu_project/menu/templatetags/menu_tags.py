from django import template
from django.urls import resolve
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if not request:
        current_url = '/'
    else:
        current_url = request.path_info

    try:
        menu_items = list(MenuItem.objects.filter(menu_name=menu_name).order_by('order'))
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        menu_items = []

    if not menu_items:
        return {
            'menu_tree': [],
            'current_url': current_url
        }

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
        for child in menu_items:
            if child.parent_id == active_item.id:
                expanded_items.add(child.id)

    def build_tree(items, parent=None, depth=0, max_depth=10):
        if depth > max_depth:
            return []
        tree = []
        for item in items:
            if item.parent_id == (parent.id if parent else None):
                children = build_tree(items, item, depth + 1, max_depth)
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