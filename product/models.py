from django.db import models
from user_account.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug= models.SlugField(unique=True, max_length=150)
    fatured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug= models.SlugField(unique=True, max_length=250)
    fatured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places = 2)
    thumbnail = models.URLField()
    img = models.ImageField(upload_to='banner', null=True, blank=True,)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True, default='N/A')
    created_date = models.DateTimeField(auto_now_add=True)
    updater_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    @property
    def related(self):
        return self.category.products.all().exclude(pk=self.pk)

class Slider (models.Model):
    title= models.CharField(max_length=50)
    banner = models.ImageField(upload_to='banner')
    show = models.BooleanField(default=True)
    creared_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title



class Order(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    

    def __str__(self):
        return 'Order # %s' % (str(self.id))

