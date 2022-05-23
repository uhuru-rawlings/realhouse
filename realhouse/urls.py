"""realhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import login_view
from signup.views import signup_view
from homepage.views import homepage_view,houses_view,logout_view,about_view,details_view,checkavailability_view
from contact.views import contact_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view , name="login"),
    path('signup/', signup_view , name="signup"),
    path('home/', homepage_view , name="home"),
    path('home/houses/', houses_view , name="houses"),
    path('home/logout/', logout_view , name="logout"),
    path('home/about/', about_view , name="about"),
    path('home/availability/', checkavailability_view , name="availability"),
    path('home/details/<int:id>/', details_view , name="details"),
    path('houses/contact/', contact_view , name="contact"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
