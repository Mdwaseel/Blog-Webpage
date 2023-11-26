from django.contrib import admin
from .models import Post,Profiles

# Register your models here
class Postadmin(admin.ModelAdmin):
    list_display = ('title','date_uploaded')



admin.site.register(Post)
admin.site.register(Profiles)