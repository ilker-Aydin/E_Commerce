from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from . import models
from . import forms
from .forms import RegisterForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm
from . forms import OrderForm
from . models import CartItem

# Create your views here.

def mainpage(request):
    return render(request,"DjangoEcommerce/mainpage.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Kayıt sonrası yönlendirilecek sayfa
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", context={"form": form})

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"

def listproducts(request):
    all_products=models.Product.objects.all()
    product_dictionary={"products":all_products}
    return render(request,'DjangoEcommerce/products.html',context=product_dictionary)
    
def product_details(request,product_id):
    product=models.Product.objects.get(pk=product_id)
    return render(request, 'DjangoEcommerce/product_details.html', context={"product": product})


'''
@login_required(login_url="/login")
def add_product(request):
    if request.POST:
        product_name = (request.POST["product_name"])
        product_describtion=(request.POST["product_describtion"])
        product_img=(request.POST["product_img"])
        product_price=(request.POST["product_price"])
        models.AddProduct.objects.create(product_name=product_name,product_describtion=product_describtion,product_img=product_img,product_price=product_price)
        return redirect(reverse('DjangoEcommerce:products'))
    else:
        return render(request, 'DjangoEcommerce/addproduct.html')
'''
@login_required(login_url="/login")
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            name=form.cleaned_data["name"]
            price=form.cleaned_data["price"]
            image=form.cleaned_data["image"]
            image2=form.cleaned_data["image2"]
            image3=form.cleaned_data["image3"]
            describtion=form.cleaned_data["describtion"]
            models.Product.objects.create(name=name,describtion=describtion,image=image,price=price,image2=image2,image3=image3,)
            return redirect(reverse('DjangoEcommerce:products'))
        else:
            print("error in form")
            return render(request,'DjangoEcommerce/addproduct.html',context={"form":form})  
    else:
        form = AddProductForm()
    return render(request, 'DjangoEcommerce/addproduct.html', context={'form': form})
@login_required(login_url="/login")
def DeleteProduct(request,id):

    product=models.Product.objects.get(pk=id)
    
   
    models.Product.objects.filter(id=id).delete()
    return redirect(reverse('DjangoEcommerce:products'))#şimdi bunu urls.py ye tanımlıca


def cart(request):
    
    cart_items = models.CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'DjangoEcommerce/cart.html', context={'cart_items': cart_items, 'total_price': total_price})
@login_required(login_url="/login")
def add_to_cart(request,product_id):
    
    product = models.Product.objects.get(id=product_id)
    cart_item, created = models.CartItem.objects.get_or_create(product=product, 
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(reverse('DjangoEcommerce:cart'))
    

def remove_from_cart(request, item_id):
    cart_item = models.CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('DjangoEcommerce:cart')

def orderform(request):
    
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    item_total_price=print((item.product.price * item.quantity for item in cart_items))

    
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = cart_item.product
            order.user = request.user
            order.save()
            return redirect('DjangoEcommerce:cart')
            
    else:
        form = OrderForm()

    context = {
        
        'form': OrderForm(),
        'cart_items': cart_items,
        'total_price': total_price,
        'item_total_price':item_total_price,
    }

    return render(request, 'DjangoEcommerce/orderform.html', context=context)
