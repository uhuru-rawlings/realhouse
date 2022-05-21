from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from signup.models import Registration

# Create your views here.
def signup_view(request):
    error = ''
    success = ''
    if request.method == 'POST':
        useremails = request.POST['useremails']
        passwords = request.POST['passwords']
        
        userexist = Registration.objects.get(useremail = useremails)
        if userexist.exists():
            error = 'user with these details provided already exist.'
        else:
            new_user = Registration(useremail = useremails, password = make_password(passwords))
            new_user.save()
            return redirect("/")
    context = {
        'title':'RealEstate - Signup'
    }
    return render(request, "signup.html",context)