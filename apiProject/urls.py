"""apiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 引入參數
from django.contrib import admin
from django.urls import path
from blog.views import *
from shop.views import *

from django.conf import settings
from django.conf.urls.static import static

# 定義URL路徑, 執行方法
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('blog/create/', post_create_view),
    path('test/', test_json_response_view),
    path('api/test/' , test_json_response_view),
    path('shop/' , shop_index)

]

# 今日重點，是我們能夠讀取到圖片的關鍵
# 將存取路徑正確地導到圖片存放的路徑
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)