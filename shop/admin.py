from django.contrib import admin

# 引入models內的Post Class
from .models import Product

# 註冊此Model Class至Admin內 使Model可進行操作
admin.site.register(Product)
