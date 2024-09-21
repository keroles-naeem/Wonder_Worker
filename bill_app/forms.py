from django.forms import ModelForm
from .models import Product,Customer


# Code added for loading form data on the Booking page
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

