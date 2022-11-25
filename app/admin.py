from django.contrib import admin

from app.models import welcome_to_admin

# Register your models here.
class appAdmin(admin.ModelAdmin):
        
    list_display=['information']
admin.site.register(welcome_to_admin,appAdmin)