from django.shortcuts import render


# 首頁
def shop_index(request):
    return render(request , 'shop/index.html')