from django import template
from treemenu.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menus = Menu.objects.prefetch_related('children').filter(menu_name=menu_name).values('id', 'name', 'parent_id', 'url')

    # Преобразуем список menus в список
    menus_list = [menu for menu in menus]

    # Соберем корневые элементы менюшек
    root_menus = [menu for menu in menus_list if menu['parent_id'] is None]

    # Найдем активный элемент меню
    active_path = context['request'].path
    active = None
    for menu in menus_list:
        if menu['url'] == active_path:
            active = menu


    # Соберем дочерних элементов для активного элемента
    tree_menu = []
    if active:
        tree_menu = [menu for menu in menus_list if menu['parent_id'] == active['id']]

    # Соберем родителей и их дочерних элементов для активного элемента вплоть до корня
    if active:
        current = active
        while current['parent_id']:
            for menu in menus_list:
                if menu['parent_id'] == current['parent_id']:
                    tree_menu.append(menu)
            for menu in menus_list:
                if menu['id'] == current['parent_id']:
                    current = menu

    # Для отображения других неактивных меню если они отрисовываются
    secondary = None
    if not tree_menu:
        for menu in root_menus:
            if menu['name'] == menu_name:
                secondary = root_menus.pop(root_menus.index(menu))
        return {'secondary': secondary}

    tree_menu = create_nested_list(tree_menu, root_menus[0]['id'])

    return {'tree_menu': tree_menu, 'root_menus': root_menus, 'active': active, 'request': context['request']}


def create_nested_list(data, parent_id):
    """Построение древовидного меню для последущего рекурсионного вызова в menu/menu_item"""
    nested_list = []
    for item in data:
        if item['parent_id'] == parent_id:
            nested_item = {key: value for key, value in item.items() if key != 'parent_id'}
            nested_item['next'] = create_nested_list(data, parent_id=item['id'])
            if not nested_item['next']:
                nested_item['next'] = []
            nested_list.append(nested_item)
    return nested_list
