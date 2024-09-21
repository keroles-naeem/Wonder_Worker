from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import Product,Order,Customer,Bill
# Register your models here.

admin.site.register(Customer)

#custumising adming panal ...
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','protien']
    list_display_links=['protien',]
    list_editable=['price']
    search_fields=['name']
    list_filter =['price']
    # fields=['name','price']

class OrderAdmin(admin.ModelAdmin):
    list_display=['order_id','customer']


class BilltAdmin(admin.ModelAdmin):
    list_display=['order_id','quantity','product','show_protien','get_total_item_price']
    list_editable=['quantity']

    # fields=['name','price']

admin.site.register(Bill,BilltAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
