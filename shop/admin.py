from django.contrib import admin

# Register your models here.
from . models import product,usersinformations,contact,bidder,winner
admin.site.register(product) 
admin.site.register(usersinformations)
admin.site.register(contact)
admin.site.register(bidder)
admin.site.register(winner)