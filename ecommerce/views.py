from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola segunda clase de django")

def segundo_template(request):
    return render(request, "template2.html", context={})