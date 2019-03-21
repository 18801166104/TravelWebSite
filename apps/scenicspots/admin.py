from django.contrib import admin

# Register your models here.
from scenicspots.models import Spots, Active

admin.site.register(Spots)
admin.site.register(Active)