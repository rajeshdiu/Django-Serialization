from django.contrib import admin

from account.models import *


class StudentAdmin(admin.ModelAdmin):
    
    list_display=['Name','Roll','City']

admin.site.register(Student_Model,StudentAdmin)