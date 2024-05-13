from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UdnFocus

# Create your views here.
def index(request):
    return render(request, "index.html")

def list(request):
    news = UdnFocus.objects.all().values()
    template = loader.get_template("list.html")
    context = {
        'news': news
    }
    # 把攜帶著資料表紀錄資料的context傳到template裡面，最後以template回應請求並顯示在瀏覽器的視窗畫面上
    return HttpResponse(template.render(context, request))


def content(request, id):
    news = UdnFocus.objects.get(id=id)
    
    # clean content
    marks = str.maketrans("","",",[]'")
    cleaned_content = news.content.translate(marks)
    
    template = loader.get_template("content.html")
    context = {
        'news': news,
        'cleaned_content': cleaned_content,
    }
    return HttpResponse(template.render(context, request))
