from django.shortcuts import render

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        useremails = request.POST['useremails']
        passwords = request.POST['passwords']
    context = {
        'title':'RealEstate - Signup'
    }
    return render(request, "signup.html",context)