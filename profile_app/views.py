from django.shortcuts import render, redirect

def index(request):
    return render(request, "main_page.html")
