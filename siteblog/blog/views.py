from django.shortcuts import render, HttpResponse


def hello(request):
    return render(request, 'blog\index.html')
