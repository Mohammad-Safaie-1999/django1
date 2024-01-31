from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email')
    ordering=['id']

admin.site.register(Contact,ContactAdmin)

