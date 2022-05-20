from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title':'RealEstate - Login'
    }
    return render(request, "login.html",context)