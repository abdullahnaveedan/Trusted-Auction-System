from django.contrib import admin

# Register your models here.
from . models import product,usersinformations,contact,bidder,bidwinners,winner
admin.site.register(product) 
admin.site.register(usersinformations)
admin.site.register(contact)
admin.site.register(bidder)
admin.site.register(bidwinners)
admin.site.register(winner)