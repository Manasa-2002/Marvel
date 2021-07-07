from django.contrib import admin
from .models import Contactcarrers,Contactservices,Contactprojects,Video

# Register your models here.

class ContactcarrersAdmin(admin.ModelAdmin):
    list_display=['Name','PhoneNumber','Email','Message']

admin.site.register(Contactcarrers,ContactcarrersAdmin) 

class ContactservicesAdmin(admin.ModelAdmin):
    list_display=['Name','PhoneNumber','Email','Message']

admin.site.register(Contactservices,ContactservicesAdmin) 

class ContactprojectsAdmin(admin.ModelAdmin):
    list_display=['Name','PhoneNumber','Email','Message']

admin.site.register(Contactprojects,ContactprojectsAdmin) 

admin.site.register(Video)