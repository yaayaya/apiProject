from django.shortcuts import render
from datetime import date
from django.views.decorators.csrf import csrf_exempt    # 跨域請求豁免
# web server gateway integrate
from django.core.handlers.wsgi import WSGIRequest

import json

from django.http import JsonResponse
from django.http import HttpRequest

from .forms import PostForm
from .models import Post


# API def
# 讓這支 API 免 csrf authentication
@csrf_exempt
def test_json_response_view(request: WSGIRequest):
    print('-----------------------------------')
    if request.method == 'GET':
        print("get GET request: ", request)
        return JsonResponse({'first': 'asdf', 'second': 'fdtest'})
    elif request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        print("get POST request data: ", data)

        # save to db
        Post.objects.create(title=data['title'], content=data['content'])

        # check posts in db
        print('all posts in db: ', Post.objects.all())

        # send response to client
        return JsonResponse({'status': 'ok, I got you.'})
    else:
        print("get unknown request: ", request)
        return JsonResponse({'status': 'no, I don\'t know it.'})


# 這次我們試著接受 Form 的 POST
# 收到的 form 如果合法，我們就存到 DB 去
def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'blog/post_create.html', context)


def hello(request):
    today = date.today().isoformat()

    context = {
        "first_var": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "second_var": 777777777777777777777777777777777777777,
        "dataList": [1, 5, 6235, 234, 23421],
        "today": today
    }

    # 表示會載入 templates內路徑 blog/index.html
    return render(request, 'blog/index.html', context)
