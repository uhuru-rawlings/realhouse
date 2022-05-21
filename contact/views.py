from django.shortcuts import render,redirect

# Create your views here.
def contact_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    context= {
        'title':'RealEstate - Contact'
    }
    return render(request, "contact.html", context)