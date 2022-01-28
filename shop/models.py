from django.db import models
from django.urls import reverse
#from django.core.urlresolvers import reverse
#from django.conf import settings
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
        args = [self.slug])
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    
    def __str__(self):
        return self.name
        
        
        
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',
        args = [self.id, self.slug])
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name


#class ProductImage(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='images')
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    #def get_absolute_url(self):
        #return reverse('shop:product_detail',
        #args = [self.id, self.slug])
    
    #def __str__(self):
        #return "%s" % self.id

    #class Meta:
        #verbose_name = 'Фотография'
        #verbose_name_plural = 'Фотографии'
