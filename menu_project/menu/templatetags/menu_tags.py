from django import template
from django.urls import resolve, NoReverseMatch
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    current_url = request.path_info if request else '/'

    menu_items = list(MenuItem.objects.filter(menu_name=menu_name).order_by('order').select_related('parent'))

    if not menu_items:
        return {'menu_tree': [], 'current_url': current_url}

    active_item = next((item for item in menu_items if item.get_url() == current_url), None)

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
                is_active = item.get_url() == current_url
                tree.append({
                    'item': item,
                    'children': children,
                    'is_expanded': item.id in expanded_items or is_active
                })
        return tree

    menu_tree = build_tree(menu_items)

    return {
        'menu_tree': menu_tree,
        'current_url': current_url
    }

def get_resolved_url(item):
    if item.named_url:
        try:
            from django.urls import reverse
            return reverse(item.named_url)
        except NoReverseMatch:
            return item.url or '#'
    return item.url or '#'