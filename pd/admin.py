from django.contrib import admin
from pd.models import Contact
from pd.models import Product
from pd.models import Category,Cart

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
