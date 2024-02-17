from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ContactUser, Store
from django.core.paginator import Paginator


def contacts(request):
    contactuser = ContactUser.objects.first()
    return render(request, 'shop/product/contakt.html',
                  {
                      'contactuser': contactuser
                  })


def home(request):
    contactuser = ContactUser.objects.first()
    return render(request, 'shop/home.html',
            {
                 'contactuser': contactuser
            })


def sergey(request):
    categories = Category.objects.filter(store=2)
    contactuser = ContactUser.objects.first()
    category = categories[0]
    store = Store.objects.filter(id=2).first()
    return render(request, 'shop/product/category.html',
                  {
                      'categories': categories,
                      'category': category,
                      'contactuser': contactuser,
                      'store': store
                  })


def hypower(request):
    categories = Category.objects.filter(store=3)
    contactuser = ContactUser.objects.first()

    store = Store.objects.filter(id=3).first()
    return render(request, 'shop/product/hypower/category.html',
                  {
                      'categories': categories,
                      'category': category,
                      'contactuser': contactuser,
                      'store': store
                  })


def plazmakroy(request):
    categories = Category.objects.filter(store=4)
    contactuser = ContactUser.objects.first()

    store = Store.objects.filter(id=3).first()
    return render(request, 'shop/product/plazmakroy/category.html',
                  {
                      'categories': categories,
                      'category': category,
                      'contactuser': contactuser,
                      'store': store
                  })


def in_cad(request):
    categories = Category.objects.filter(store=5)
    contactuser = ContactUser.objects.first()

    store = Store.objects.filter(id=5).first()
    return render(request, 'shop/product/incad/category_nophoto.html',
                  {
                      'categories': categories,
                      'category': category,
                      'contactuser': contactuser,
                      'store': store
                  })


def cryobak(request):
    products = Product.objects.filter(store=1)
    store = Store.objects.filter(id=1).first()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product/cryobak/cryobak.html',
                  {
                      'product': products,
                      'page_obj': page_obj,
                      'store': store
                  })


def cryobak_products(request):
    products = Product.objects.filter(store=1)
    store = Store.objects.filter(id=1).first()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product/cryobak/cryobak_products.html',
                  {
                      'product': products,
                      'page_obj': page_obj,
                      'store': store
                  })


def consumables(request):
    categories = Category.objects.filter(store=3)
    contactuser = ContactUser.objects.first()
    category = categories[0]
    return render(request, 'shop/product/category.html',
                  {
                      'categories': categories,
                      'category': category,
                      'contactuser': contactuser
                  })


def category(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    store = Store.objects.all()
    return render(request, 'shop/product/category.html',
                  {
                      'categories': categories,
                      'products': products,
                      'store': store
                  })


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    contactuser = ContactUser.objects.first()
    return render(request, 'shop/product/my_list_all.html',
                  {
                      "page_obj": page_obj,
                      'contactuser': contactuser
                  })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product/my_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      "page_obj": page_obj
                  })


def product_list_nophoto(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product/incad/my_list_unphoto.html',
                  {
                      'category': category,
                      'categories': categories,
                      "page_obj": page_obj
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.all()
    contactuser = ContactUser.objects.first()
    return render(request, 'shop/product/my_detail.html',
                  {
                      'product': product,
                      'products': products,
                      'contactuser': contactuser
                  })


def cryobak_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.all()
    contactuser = ContactUser.objects.first()
    store = Store.objects.filter(id=1).first()
    return render(request, 'shop/product/cryobak/cryobak_detail.html',
                  {
                      'product': product,
                      'products': products,
                      'contactuser': contactuser,
                      'store': store
                  })


