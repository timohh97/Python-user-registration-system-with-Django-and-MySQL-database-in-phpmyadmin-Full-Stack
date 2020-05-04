from django.shortcuts import render


def initStartPage(request):
    return render(request,"registration/index.html")
