from django import template
from django.urls import NoReverseMatch
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    current_path = request.path_info if request else '/'

    items_qs = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('order', 'id')
    items = list(items_qs)

    if not items:
        return {'menu_tree': [], 'menu_name': menu_name, 'current_path': current_path}

    id_to_url = {}
    for it in items:
        try:
            id_to_url[it.id] = it.get_url()
        except NoReverseMatch:
            id_to_url[it.id] = it.url or '#'

    active_item = None
    best_len = -1
    for it in items:
        u = id_to_url.get(it.id, '#')
        if u == current_path:
            active_item = it
            best_len = len(u)
            break
        if u != '#' and current_path.startswith(u.rstrip('/') + '/') or (u.endswith('/') and current_path.startswith(u)):
            l = len(u)
            if l > best_len:
                active_item = it
                best_len = l

    expanded = set()
    if active_item:
        cur = active_item
        while cur:
            expanded.add(cur.id)
            cur = cur.parent
        for it in items:
            if it.parent_id == active_item.id:
                expanded.add(it.id)

    by_parent = {}
    for it in items:
        by_parent.setdefault(it.parent_id, []).append(it)

    def build_nodes(parent_id):
        nodes = []
        children = by_parent.get(parent_id, [])
        for it in children:
            url = id_to_url.get(it.id, '#')
            is_active = (url == current_path) or (url != '#' and (current_path.startswith(url.rstrip('/') + '/') or current_path.startswith(url) and url.endswith('/')))
            node_children = build_nodes(it.id)
            node = {
                'id': it.id,
                'title': it.title,
                'url': url,
                'children': node_children,
                'is_active': is_active,
                'is_expanded': (it.id in expanded) or is_active,
            }
            nodes.append(node)
        return nodes

    menu_tree = build_nodes(None)
    return {'menu_tree': menu_tree, 'menu_name': menu_name, 'current_path': current_path}
