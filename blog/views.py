from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    articel = models.Article.objects.get(pk=1);
    return render(request,'blog/index.html',{'articel':articel})

