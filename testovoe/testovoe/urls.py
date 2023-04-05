from django.contrib import admin
from django.urls import path, include

from treemenu.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<str:menu_name>/', index, name='menu'),
    path('__debug__/', include('debug_toolbar.urls')),
]
