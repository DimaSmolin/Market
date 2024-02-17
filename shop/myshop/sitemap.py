from django.contrib.sitemaps import Sitemap
from .models import Category, Product


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()
    def location(self, obj):
        return obj.get_absolute_url()
    def lastmod(self, obj):
        return obj.uploaded
