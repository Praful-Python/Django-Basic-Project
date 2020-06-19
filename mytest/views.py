from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Product

# Create your views here.


def index(request):
    str = """<script>window.location = "/mytestbasic/"</script>"""
    return HttpResponse(str)