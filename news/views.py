from django.shortcuts import render
from .models import TopPost, Posts


# Create your views here.
def index(request):
    new = Posts.objects.all()
    top = TopPost.objects.all()
    news = {
        'new': new,
        'top': top
    }
    return render(request=request, template_name='home.html', context=news)


def post_detail(request, id):
    new = Posts.objects.get(id=id)
    top = TopPost.objects.all()
    news = {
        'new': new,
        'top': top
    }
    return render(request=request, template_name='post_detail.html', context=news)


def login(request):
    return render(request=request, template_name='login.html')