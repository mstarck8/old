
from django.shortcuts import render


def index(request):
    return render(request, 'news/base.html')





