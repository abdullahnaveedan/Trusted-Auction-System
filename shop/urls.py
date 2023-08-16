from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("bidding/",views.bidding, name="bidding"),
    path("login/",views.login, name = "login"),
    path("signup/",views.signup, name = "signup"),
    path("products/<int:myid>",views.products,name = "Products"),
    path("contactform",views.contactform,name = "contactform"),
    path("signuptobid",views.signuptobid,name = "signuptobid"),
    path("sellermode/",views.sellermode,name = "sellermode"),
    path("productdata/",views.productdata,name = "productdata"),
    path("login/",views.login,name = "productdata"),
    path("loginvalidation/",views.loginvalidation,name = "logedin"),
    path("logoutvalidate/",views.logoutvalidate,name = "logedout"),
    path("submitbid/" , views.submitbid, name = "submitbid"),
    path("dashboard/" , views.dashboard, name = "dashboard"),
    path("mybids/" , views.mybids, name = "mybids"),
    path("results/" , views.results, name = "results"),
    path("results/<int:myid>" , views.closebid, name = "closebid"),
] +  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

