from django.shortcuts import render

# Create your views here.
def contact_view(request):
    context= {
        'title':'RealEstate - Contact'
    }
    return render(request, "contact.html", context)