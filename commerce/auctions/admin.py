from django.contrib import admin
from .models import User, auctionlist, bids, comments

# Register your models here.
admin.site.register(User)
admin.site.register(auctionlist)
admin.site.register(bids)
admin.site.register(comments)