from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("administratorlogintowebsite/", admin.site.urls),   
    path("",views.index,name="home"),
    path("shop/",include('shop.urls')),
    path("blog/",include('blog.urls')),
    path("about/",views.about,name="about"),
    path("goals/",views.goals,name="goals"),
    path("contact/",views.contact,name="contact"),
    path("contactform",include('shop.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
