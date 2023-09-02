from django.db import models

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50, default = "")
    sub_catagory = models.CharField(max_length=50, default = "")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=1000)
    images = models.ImageField(upload_to="shop/images/%y",default = "", height_field=None, width_field=None, max_length=None)
    useremail = models.CharField(max_length=50, default = "")
    
    def __str__(self):
        return self.product_name

class usersinformations(models.Model):
    user_id = models.AutoField
    userfname = models.CharField(max_length=50,default="")
    userlname = models.CharField(max_length=50, default = "")
    useremail = models.CharField(max_length=50, default = "")
    phonenumber = models.IntegerField(default = 0)
    useraddress = models.CharField(max_length=300,default="")
    usercity = models.CharField(max_length=50,default="")
    userpassword = models.CharField(max_length=50,default="")

    def __str__(self):
        fullname = self.userfname + ' ' + self.userlname
        return fullname

class contact(models.Model):
    msgid = models.AutoField 
    useremail = models.CharField(max_length=50, default = "")
    subject = models.CharField(max_length=50,default="")
    message = models.CharField(max_length=1000,default="")
    
    def __str__(self):
        return self.subject
class bidder(models.Model):
    bid = models.AutoField(primary_key = True)
    pid = models.CharField(max_length=50)
    bemail = models.EmailField(max_length=254)
    bprice = models.CharField(max_length=50)

    def __str__(self):
        return self.pid
    
class winner(models.Model):
    productid = models.AutoField(primary_key = True)
    productname = models.CharField(max_length=50)
    owneremail = models.CharField(max_length=50)
    winneremail = models.CharField(max_length=50)
    price = models.CharField(max_length = 50)
    phonenumber = models.IntegerField(default = 0)
    def __str__(self):
        return self.productname
    