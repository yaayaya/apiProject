# shop/test/test_models.py

# 引入django 單元測試
from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField
# 目標 Model
from shop.models import Product

# (TestCase)會去跑class裡面跑一遍
class TestProductFieldType(TestCase):
    def test_name_field_type(self):
        assert_same_type(self, "name", CharField)

    def test_price_field_type(self):
        assert_same_type(self, "price", DecimalField)

    def test_img_field_type(self):
        assert_same_type(self, "img", ImageField)

    def test_onsale_field_type(self):
        assert_same_type(self, "on_sale", BooleanField)


# assertTrue(Bool)  instance判斷狀態(value,type)
def assert_same_type(self, field_name, field_type):
    self.assertTrue(
        isinstance(
            get_product_field(field_name),
            field_type
        )
    )
    print(isinstance(1234, int))

# 抓取DB格式 特定欄位名稱
def get_product_field(field_name):
    return Product._meta.get_field(field_name)
