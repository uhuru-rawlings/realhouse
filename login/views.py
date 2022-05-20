from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.
def login_view(request):
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
    context = {
        'title':'RealEstate - Login'
    }
    return render(request, "login.html",context)