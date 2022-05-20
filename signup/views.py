from django.shortcuts import render

# Create your views here.
def signup_view(request):
    context = {
        'title':'RealEstate - Signup'
    }
    return render(request, "signup.html",context)