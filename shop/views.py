from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,contact,usersinformations, bidder , winner
from math import ceil
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def bidding(request):
    allprod = []
    catprods = product.objects.values('catagory','id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(catagory = cat)
        n= len(prod)
        nSlides= n//4 + ceil(n/4 - n//4)
        allprod.append([prod,range(1,nSlides),nSlides])
    params = {'allprod':allprod}
    return render(request,"shop/index.html", params)


def products(request,myid):
    prods = product.objects.filter(id=myid)
    param = {'productview' : prods[0] , 'pid' : myid}
    return render(request,"shop/productview.html",param)

def login(request):
    return render(request,"shop/login.html")

def signup(request):
    return render(request,"shop/signup.html")
    
def signuptobid(request):
    if request.method == 'POST':
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1 == pass2):
            fname = request.POST.get('fname', '')
            lname = request.POST.get('lname' , '')
            email = request.POST.get('email', '')
            address = request.POST.get('address','')
            city = request.POST.get('city' , '')
            number = request.POST.get('number','')
            userinfo = usersinformations(userfname = fname, userlname = lname, useremail = email, phonenumber = number, useraddress = address, usercity = city, userpassword = pass1)
            userinfo.save()
            username = lname + fname + '1'
            myuser = User.objects.create_user(username,email,pass2)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = authenticate(request , username = username , password = pass1)
            auth_login(request , user)    
            return redirect("bidding")
        else:
            return HttpResponse("<h1>Password not same</h1>")
    else:
        return HttpResponse("<h1>Error-404</h1>")

def contactform(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        subject = request.POST.get('subject' , '')
        message = request.POST.get('message','')
        contacts = contact(useremail = email, subject = subject , message = message)
        contacts.save()
        #message.success(request , "Your Query is been processed")
        return render(request,"contact.html")
    else:
        return HttpResponse("<h1>Error 404 Page not found</h1>")

def sellermode(request):
    wer = request.user
    em = (wer.email)
    param = {'email' : em}
    return render(request , "shop/saller.html",param)

def productdata(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        catagory = request.POST.get('catagory','')
        subcatagory = request.POST.get('subcatagory','')
        price = request.POST.get('price','')
        desc = request.POST.get('desc','')
        email = request.POST.get('email','')
        # image = '/media/shop/images/'+ request.FILES.get('image','')
        # image = request.FILES.get('image', '')
        
        image_file = request.FILES.get('image', None)
        if image_file:
            # Generate a unique file name or use the original file name
            file_name = default_storage.save('shop/images/' + image_file.name, ContentFile(image_file.read()))
            image = file_name
        else:
            image = ''
        
        print("**" , image , "**" )

        p1 = product(product_name = name, catagory = catagory, sub_catagory = subcatagory,price=price, desc=desc, images = image, useremail = email)
        p1.save()
    else:
        return HttpResponse("<h1>Error 404 Page not found</h1>")
    return redirect("bidding")
        
def login(request):
    return render(request , "shop/login.html")

def loginvalidation(request):
    if request.method == "POST":
        username = request.POST['inputusername']
        password = request.POST['inputPassword']
        user = authenticate(request,username = username , password = password)
        print(username,password)
        if user:
            auth_login(request,user)
            return redirect("bidding")
        else:
            return HttpResponse("<h1>Error 4045 Page found</h1>")
    else:
        return HttpResponse("<h1>Error 4045 Page found</h1>")

def logoutvalidate(request):
    logout(request)
    return render(request , "index.html")
def submitbid(request):
    wer = request.user
    em = (wer.email)
    if request.method == 'POST':
        pid = request.POST.get('pid')
        price = request.POST.get('bidprice')
        data = product.objects.filter(id = pid)
        if data[0].price < int(price):
            bid = bidder(pid = pid, bemail = em, bprice = price)
            bid.save()
            return redirect("dashboard")
    return HttpResponse("<h1>Price Issue</h1>")

def data(request):
    wer = request.user
    em = (wer.email)
    da = bidder.objects.filter(bemail = em)
    count = da.count()
    if count == 0:
        param = { 'count' : count}
    else:
        prod = product.objects.filter(id = da[0].pid)
        param = {'bidding':da , 'nameprod' : prod[0]}
    return render(request,"shop/data.html",param)

def dashboard(request):
    wer = request.user
    email = (wer.email)
    objs = bidder.objects.filter(bemail = email)
    bidd = objs.count()
    objs = product.objects.filter(useremail = email)
    prods = objs.count()
    objs = winner.objects.filter(winneremail = email)
    win = objs.count()
    total_price = winner.objects.filter(owneremail=email).aggregate(total_price=Sum('price'))
    t_earn = total_price['total_price'] 
    if t_earn == None:
        t_earn = 0
    
    
    param = {'username' : request.user.username, 'bids' : bidd, 'product' :prods, 'earn' : t_earn , 'email':email,'win':win}
    return render(request,"shop/dashboard.html",param)

def mybids(request):
    wer = request.user
    em = (wer.email)
    da = bidder.objects.filter(bemail = em)
    count = da.count()
    if count == 0:
        param = { 'countda' : count}
    else:
        prod = product.objects.filter(id = da[0].pid)
    objs = winner.objects.filter(winneremail = em)
    param = {'bidding':da , 'nameprod' : prod[0],'objs':objs,'countda' : count , 'countobj':objs.count()}
    return render(request,"shop/mybids.html",param)

def results(request):
    wer = request.user
    email = (wer.email)
    objs = product.objects.filter(useremail = email)
    arrforbids = []
    arrformax = []
    
    for obj in objs:
        bid_objs = bidder.objects.filter(pid=obj.id)
        arrforbids.append(bid_objs.count())
        if bid_objs.exists():
            max_price = max(bid_obj.bprice for bid_obj in bid_objs)
            arrformax.append(max_price)
        else:
            arrformax.append(0)
        # for bid_obj in bid_objs:
        #     print('arrforbids:', arrforbids)
        #     print('bprice:', bid_obj.bprice)
        #     print('bemail:', bid_obj.bemail)
    # print(arrformax)
    # for i in objs:
    #     obj = bidder.objects.filter(pid = i.id)
    #     arrforbids.append(obj.count())
    #     buffer=bidder.objects.all()
    #     print("**")
    #     for item in buffer:
    #         print(item.bemail,'**')
            
    zipper = zip(objs,arrforbids,arrformax)
    params = {'count' : objs.count(), 'zipp':zipper}
    ob = bidder.objects.all()
    return render(request,"shop/results.html",params)

def closebid(request,myid):
    obj = product.objects.filter(id = myid)
    objs = bidder.objects.filter(pid = myid)
    max_price = 0
    if objs.count() == 0:
        return render(request,"shop/sorry.html")
    else:
        max_price = max(objs.bprice for objs in objs)

    objs = bidder.objects.filter(bprice = max_price)
    mail = obj[0].useremail
    user = usersinformations.objects.filter(useremail = mail)
    
    data = winner(productid = myid,productname = obj[0].product_name, owneremail = obj[0].useremail,winneremail = objs[0].bemail,price = max_price,
    phonenumber = user[0].phonenumber)
    data.save()

    objs = winner.objects.filter(productid = myid)
    param = {'product' : obj[0],'data':objs[0]}
    instance = bidder.objects.filter(pid=myid)
    instance.delete()

    return render(request,"shop/closebid.html",param)