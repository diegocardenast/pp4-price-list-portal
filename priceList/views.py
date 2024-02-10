from django.shortcuts import render
from priceList.views import HttpResponse

# Create your views here.
def my_priceList(request):
    return HttpResponse("Hello, Plastilecor!");