
from django.urls import path
from pd import views
from django.conf import settings
from  django.conf.urls.static import static



urlpatterns = [
    
    
    path('',views.index,name='home'),
    path('home/',views.index, name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='about'), 
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('search/',views.search,name='search'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('place-order/', views.place_order, name='place_order'),  # Cash on Delivery
    path('online-payment/', views.online_payment, name='online_payment'),  # Online Payment
    
   
   
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)