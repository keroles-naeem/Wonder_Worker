from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
   customer_name=models.CharField(max_length=20)   
   customer_number=models.IntegerField(primary_key=True)
   cus_note=models.CharField(max_length=20,null=True)
   # cus_paid=models.IntegerField(default=0)
   cus_acc=models.IntegerField(default=0)
   

   
   def __str__(self):
      return self.customer_name 


class Product(models.Model):
   id=models.AutoField(primary_key=True)
   name = models.CharField(max_length=200)
   protien=models.DecimalField(max_length=1,null=True,decimal_places=2,max_digits=5)
   weight=models.CharField(max_length=5 )
   price = models.IntegerField(null=False)
   quantity = models.IntegerField(default=1)
   def get_total_item_price(self):
      return self.quantity * self.price
   def __str__(self):
      return self.name 
   

class Order(models.Model):
   order_id=models.AutoField(primary_key=True)
   order_date=models.DateField(default=timezone.now)
   customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
   def __str__(self):
      return self.customer.customer_name 


class Bill(models.Model):
   order=models.ForeignKey(Order,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   cus_paid=models.IntegerField(default=0)
   class Meta:
      unique_together = ('order', 'product')
   def get_total_item_price(self):
      return self.quantity * self.product.price
   def show_protien(self):
      return self.product.protien

   def __str__(self):
      return self.order.customer.customer_name
    

# class Bills_archive(models.Model):
#    order_id=models.ForeignKey(Order)
#    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)
#    cus_paid=models.IntegerField(default=0)