from django.shortcuts import render


def index(request, menu_name='main_menu'):
    context = {'menu_name': menu_name}
    return render(request, 'index.html', context)
