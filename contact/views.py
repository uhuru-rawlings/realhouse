from django.shortcuts import render,redirect

from contact.models import Contactus

# Create your views here.
def contact_view(request):
    try:
        user = request.COOKIES['userde']
    except:
        return redirect("/")
    success = ''
    if request.method  == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailadress = request.POST['emailadress']
        phonenumber = request.POST['phonenumber']
        messages = request.POST['messages']

        new_contact = Contactus(firstname = firstname,lastname = lastname,emailadress = emailadress,phonenumber = phonenumber,messages = messages)
        new_contact.save()

        success = 'contact form sent successfully.'
    context= {
        'title':'RealEstate - Contact',
        'success':success
    }
    return render(request, "contact.html", context)