from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductForm ,UserForm
from .models import Product,Bill,Order,Customer



# Create your views here.

def product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'add_product.html', context)

def home(request):
    return render(request, 'index.html')

# Add your code here to create new views
def products(request):
    products_items=Product.objects.all()
    total=0
    for i in products_items:
        if i is None:
            return total
        else:
            total+=i.get_total_item_price()
    products_dect={'product':products_items,'total':total}   
    return render(request, 'products.html',products_dect)

def users(request):
    users=Customer.objects.all()
    users_dect={'users':users}   
    return render(request, 'users.html',users_dect)

def user_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'user_page.html', context)


def order_id(request):
    if request.method=="POST" :
        order_id=request.POST['order']
        # order_obj=Order.objects.filter(order_id=order_id)
        bill_obj=Bill.objects.filter(order=order_id)
        total=0
        for i in bill_obj:
            if i is None:
                return total
            else:
                total+=i.get_total_item_price()
                
        products_dect={'product':bill_obj,'total':total}
        return render(request, 'bill_view.html',products_dect)

    else:
        return render(request, 'bill_id.html')


def create_order(request):
    if request.method=="POST" :
        try:
            cus_name=request.POST['customer']
            cus_obj=Customer.objects.get(customer_name=cus_name)
            Order.objects.create(customer=cus_obj)
            return redirect("billing")
        except ObjectDoesNotExist :
            return render(request,'pageNotFound.html')
    else:
        customers=Customer.objects.all()
        options={'customers':[]}
# show option in the templete
        for i in customers :
            if i.customer_name not in options['customers']:
                options['customers'].append(i.customer_name)
    products_dect={'options':options} 
    return render(request, 'create_order.html',products_dect)


def billing(request):
    options={"protien":[], "weight":[], "name":[],'customers':[]}
    product=Product.objects.all()
    bill = Bill.objects.filter(order=Order.objects.last())
    for i in product:
        if i.protien not in options['protien']:
            options['protien'].append(i.protien)
        if i.weight not in options['weight']:
            options['weight'].append(i.weight)
        if i.name not in options['name']:
            options['name'].append(i.name)
 

# getting the order_id if order exists
    if Order.objects.exists():
        order_id=Order.objects.last().order_id
    else:
        order_id=0
        
    total=0
    for i in bill:
        if i is None:
            return total
        else:
            total+=i.get_total_item_price()
    products_dect={'product':Bill.objects.filter(order=Order.objects.last()),'total':total,'order_id':order_id,'options':options} 
    if request.method=="POST" :
        value=request.POST.get('account', False)
        print(value)
        return render(request, 'success.html',products_dect)
    else:
        return render(request,'bill.html',products_dect)
    
def add_to_bill(request):
    if request.method=="POST":
        weight=request.POST['weight']
        name=request.POST['name']
        protien=request.POST['protien']
        add_quantity=request.POST['quantity']
        
        try:
            item = Product.objects.get(name=name,weight=weight,protien=protien)
            price=item.price * int(add_quantity)
        except ObjectDoesNotExist :
            return render(request,'pageNotFound.html')

        
        try:
            add_customer=Customer.objects.get(customer_number='01210336070')
        except ObjectDoesNotExist:
            add_customer=Customer.objects.create(customer_number="01210336070",customer_name="keroles_naeem")
        if Order.objects.exists():
            add_order=Order.objects.last()
        else:
            add_order=Order.objects.create(customer=add_customer)
        try:    
            Bill.objects.create(
                order=add_order,
                product=item,
                quantity=int(add_quantity),
                price=int(price)
            )
        except:
            redirect("billing")
        return redirect("billing")


def remove_product(request, order_id, product_id):
    order=Order.objects.get(order_id=order_id)
    product=Product.objects.get(id=product_id)
    # Remove the product from the bill
    bill=Bill.objects.filter(order=order,product=product)
    bill.delete()
    # Save the updated bill object
    return redirect('billing')

def quantity_controller(request,order_id, product_id,operation):
    order=Order.objects.get(order_id=order_id)
    product=Product.objects.get(id=product_id)
    bill=Bill.objects.filter(order=order,product=product)[0]
    if bill.quantity>1:
        if operation==1:
            bill.quantity+=1
            bill.save()
        else:
            bill.quantity-=1
            bill.save()

    else:
        bill.delete()
    return redirect('billing')
# update the inventory delete 
def update_products(request):
    bill=Bill.objects.all()
    for item in bill:
        product=Product.objects.get(id=item.product.id)
        product.quantity-=item.quantity
        product.save()
    order=Order.objects.get(order_id=item.order.order_id)
    order.save()
    return redirect('create_order')
