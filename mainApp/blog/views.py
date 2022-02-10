from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your view  here
def index(request):
    return HttpResponse("Main Screen!!")


def search(request):
    keyword = request.GET['search_value']


def create(request):
    new_blog = Blog() # 데이터 저장을 위한 객체 생성
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save() # 객체 저장
    return redirect('detail', new_blog.id)