from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.home, name='home'),
    path('lasermashines', views.sergey, name='sergey'),
    path('hypower', views.hypower, name='hypower'),
    path('plazmakroy', views.plazmakroy, name='plazmakroy'),
    path('in-cad', views.in_cad, name='in_cad'),
    path('cryobak', views.cryobak, name='cryobak'),
    path('cryobak_products', views.cryobak_products, name='cryobak_products'),
    path('consumables', views.consumables, name='consumables'),
    path('category', views.category, name='category'),
    path('products', views.all_products, name='products'),
    path('contacts', views.contacts, name='contacts'),

    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('in-cab/<slug:category_slug>/', views.product_list_nophoto,
         name='product_list_by_category_nophoto'
         ),
    path('product/<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
    path('cryobak/<int:id>/<slug:slug>', views.cryobak_detail,
         name='cryobak_detail'),
]

