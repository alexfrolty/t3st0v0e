example create tree menu:
http://127.0.0.1:8000/admin/treemenu/menu/add/
```
Name: products
Url: /products/ or Named url: products
Parent: -
Menu name: products

  Name: fruits
  Url: /fruits/ or Named url: fruits
  Parent: products
  Menu name: products

    Name: bananas
    Url: /bananas/ or Named url: bananas
    Parent: fruits
    Menu name: products
```

```
index.html

{% load menu %}

{% draw_menu 'products' %}
```
