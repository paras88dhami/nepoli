from django.shortcuts import render, redirect,HttpResponse
from pd.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from pd.models import Product,Category,Cart
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    products=Product.objects.all()
    

    return render(request, 'home.html',{'products':products})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Message sent successfully!")
    return render(request, 'contact.html')

def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'shop.html',{'products':products,'category':category})

    except:
      messages.success(request, "that category dosen't exist")
    
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


            
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in")

            # Redirect to the 'next' parameter if it exists, else go to home page
            next_url = request.GET.get('next', '/')
            return redirect(next_url)  # Redirects to the page the user was trying to access

        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    # Render the login page for GET requests
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        userr = User.objects.create_user(username=username, email=email, password=password)
        userr.save()
        return redirect('login')
        
    return render(request, 'signup.html')
  


def search(request):
    
    if request.method == "POST" or request.method == "GET":
        searched = request.GET.get('searched') or request.POST.get('searched')
        if searched:
            products = Product.objects.filter(name__icontains=searched)
        else:
            products = []
        return render(request, 'search.html', {'searched': products, 'query': searched})
    else:
        return render(request, 'search.html', {'searched': [], 'query': ''})


def product(request,pk):
    product=Product.objects.get(id=pk)
    

    return render(request,'details.html',{'product':product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f"{product.name} has been added to your cart.")
    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
    return redirect('cart')



# Place Order with Cash on Delivery
@login_required
def place_order(request):
    if request.method == 'POST':
        # Handle the order placement with Cash on Delivery
        # For example, create an Order and set payment status to 'COD'
        # You can redirect to a confirmation page or back to home
        messages.success(request, "Successfully logged ordered")
        return redirect('cart')  # Replace with your actual URL

# Handle Online Payment
@login_required
def online_payment(request):
    if request.method == 'POST':
        # Handle the online payment process
        # Integrate with a payment gateway like Stripe or Razorpay
        # You can redirect to a payment page or gateway
        return redirect('payment_gateway.html')  # Replace with your actual payment handling URL
# Handle Cash on Delivery
