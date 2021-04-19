from django.contrib import admin

# Register your models here.
from .models import Userinfo, Usertype, Bookhouse, Buyer, \
    Agencycomp, Agencyinfo, Decoration, Houseinfo, Housetype, \
    Ownership, Publishhouse, Starhouse

admin.site.register(Userinfo)
admin.site.register(Usertype)
admin.site.register(Bookhouse)
admin.site.register(Buyer)
admin.site.register(Agencycomp)
admin.site.register(Agencyinfo)
admin.site.register(Decoration)
admin.site.register(Houseinfo)
admin.site.register(Housetype)
admin.site.register(Ownership)
admin.site.register(Publishhouse)
admin.site.register(Starhouse)