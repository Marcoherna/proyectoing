from django.shortcuts import render
from django.urls import reverse


def productos (request):
    context={}
    return render (request, "productos/producto.html", context)