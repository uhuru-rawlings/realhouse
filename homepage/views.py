from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    context = {
        'title':'RealEstate - Home Page'
    }
    return render(request,"homepage.html",context)


def houses_view(request):
    context = {
        'title':'RealEstate - Homes'
    }
    return render(request,"houses.html",context)