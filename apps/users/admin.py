from django.contrib import admin

# Register your models here.
from users.models import MyUser, Banner, TheContact

admin.site.register(MyUser)
admin.site.register(Banner)
admin.site.register(TheContact)