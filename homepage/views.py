from django.shortcuts import redirect, render
from homepage.models import Houses,Availability
from django.db.models import Q
# Create your views here.
def homepage_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    homes = Houses.objects.all().order_by('-id')[:4]
    context = {
        'title':'RealEstate - Home Page',
        'homes':homes,
    }
    return render(request,"homepage.html",context)


def houses_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    homes = Houses.objects.all()
    posts = ''
    searchhomes = ''
    if request.method == 'POST':
        location = request.POST['location']
        types = request.POST['types']
        price = request.POST['price']

        searchhomes = Houses.objects.filter(Q(location = location) | Q(price = price) | Q(choices = types))
        posts = 'posted'
    context = {
        'title':'RealEstate - Homes',
        'homes':homes,
        'posts':posts,
        'searchhomes':searchhomes
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


def details_view(request,id):
    homes = Houses.objects.get(id = id)
    texts = 'I saw this nice home at realestate and i am interested. can we link up?'
    context = {
        'title':'RealEstate - Details',
        'house':homes,
        'texts':texts
    }
    return render(request,"details.html", context)

def checkavailability_view(request):
    if request.method == 'POST':
        useremails = request.POST['useremails']
        telephoneno = request.POST['telephoneno']
        availabilitymessage = request.POST['availabilitymessage']

        new_check = Availability(useremails = useremails,telephoneno = telephoneno,availabilitymessage = availabilitymessage)
        new_check.save()

        return redirect('houses')