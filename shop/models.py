from django.db import models
from django.utils import timezone
import os

# 產品圖片的存放路徑是 media/uploads/xxx.jpg，
# 而存放在 DB 的路徑是 uploads/xxx.jpg
# 所以我們在 html 使用時，需要自己補 /media/ 的前綴
# 在 html 的完整使用是 /media/{product.0.img}

# 取得圖片路徑()
def get_image_path(instance, filename):
    return os.path.join('uploads', filename)


class Product(models.Model):
    # CharField 文字屬性  
    # basic info，基本屬性
    name = models.CharField(
        max_length=10, blank=False
    )
    # max_digits:最大數字數量   10**n
    # decimal_places 最大小數點數 
    price = models.DecimalField(
        blank=False, max_digits=100, decimal_places=0
    )
    img = models.ImageField(
        upload_to=get_image_path,
        default=get_image_path(
            instance=0, filename='product-1.jpg'
        )
    )

    # discount，跟折扣相關的屬性
    on_sale = models.BooleanField(
        blank=True, null=True
    )
    
    tag = models.CharField(
        max_length=20, blank=True, null=True
    )
    percent_off = models.DecimalField(
        blank=True, null=True, max_digits=30, decimal_places=1
    )
    sale_price = models.DecimalField(
        blank=True, null=True, max_digits=30, decimal_places=0
    )

    # for analysis，網頁使用者看不到，但可事後分析的屬性
    bought_counter = models.DecimalField(
        default=0, max_digits=30, decimal_places=0
    )
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.name
