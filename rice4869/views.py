from django.shortcuts import render


def index(request):
    return render(request, 'rice4869/index.html')
