from django.db import models
from django.urls import reverse


class Store(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(max_length=3000, blank=True, null=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Category(models.Model):
    store = models.ForeignKey(Store,
                              related_name='categories',
                              on_delete=models.CASCADE,
                              null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])

    def get_another_url(self):
        return reverse('myshop:product_list_by_category_nophoto', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 null=True, blank=True)

    store = models.ForeignKey(Store,
                              related_name='products_store',
                              on_delete=models.CASCADE,
                              null=True, blank=True)

    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    description_2 = models.TextField(max_length=2000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])

    def get_another_url(self):
        return reverse('myshop:cryobak_detail', args=[self.id, self.slug])


class ContactUser(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Контактный пользователь'
        verbose_name_plural = 'Контактные пользователи'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    alt = models.CharField(max_length=100)
    store = models.ForeignKey(Store,
                              related_name='photo_store',
                              on_delete=models.CASCADE,
                              null=True, blank=True)


    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name
