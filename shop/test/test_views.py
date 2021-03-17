# shop/test/test_views.py

from django.test import TestCase
from django.urls import resolve

from shop.views import shop_index

# TestCase走進去裡面跑一圈 錯誤回傳
class TestShopPageView(TestCase):
    def test_resolve_shop(self):
        found = resolve('/shop/')
        self.assertEqual(found.func.__name__, shop_index.__name__) 
		# 期望 found.func.__name__ 會等於 shop_index

    def test_reachable_shop(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
		# 期望 status_code 會等於 200 (也就是正常)

    def test_template_shop(self):
        response = self.client.get('/shop/')
        self.assertTemplateUsed(response, 'shop/index.html')
		# 期望這頁面的 template 是 shop/index.html 這個檔案

    def test_title_shop(self):
        response = self.client.get('/shop/')
        self.assertContains(response, 'testTitle')
        print(response)
		# 期望這頁面的標題是 testTitle
