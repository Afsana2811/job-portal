from django.contrib import admin
from .models import *
admin.site.register(employer)
admin.site.register(employee)
class employees(admin.ModelAdmin):
    list_display=('name','phone','email','address','occupation','experience')
# Register your models here.
