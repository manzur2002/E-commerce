from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slider)
admin.site.register(Order)
