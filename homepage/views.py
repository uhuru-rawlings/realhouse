from django.shortcuts import redirect, render

# Create your views here.
def homepage_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    context = {
        'title':'RealEstate - Home Page'
    }
    return render(request,"homepage.html",context)


def houses_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    context = {
        'title':'RealEstate - Homes'
    }
    return render(request,"houses.html",context)


def logout_view(request):
    response = redirect('/')
    response.delete_cookie("userde")
    return response


def about_view(request):
    context = {
        'title':'RealEstate - About us'
    }
    return render(request,"about.html", context)