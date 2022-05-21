from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password

from signup.models import Registration



# Create your views here.
def login_view(request):
    error = ''
    success = ''
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']

        userexist = Registration.objects.filter(useremail = useremail)
        if userexist.exists():
            user = Registration.objects.get(useremail = useremail)
            if check_password(password, user.password):
                response = redirect('/home/')
                response.set_cookie("userde",useremail)
                return response
            else:
                error = 'Wrong login details provided.'
        else:
            error = 'user with these details dont exist'
    context = {
        'title':'RealEstate - Login'
    }
    return render(request, "login.html",context)