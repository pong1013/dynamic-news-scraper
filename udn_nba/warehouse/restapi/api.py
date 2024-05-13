from rest_framework.decorators import api_view
from ..models import UdnFocus
from .serializer import UdnFocusSerializer
from django.shortcuts import render

@api_view(['GET'])
def news_list(request):
    news = UdnFocus.objects.all()
    serializer = UdnFocusSerializer(news, many=True)
    context = {
        'news': serializer.data
    }
    return render(request, 'list.html', context)

@api_view(['GET'])
def news_detail(request, id):
    news = UdnFocus.objects.get(id=id)
    
    # clean content \
    marks = str.maketrans("","",",[]'")
    cleaned_content = news.content.translate(marks)
    
    # serializer data
    serializer = UdnFocusSerializer(news)
    
    context = {
        'news': serializer.data,
        'cleaned_content': cleaned_content,
    }
    return render(request, 'content.html', context)