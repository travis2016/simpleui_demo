from django.contrib import admin
from interface_test.models import message
# Register your models here.



@admin.register(message)
class interfacemessage(admin.ModelAdmin):
    list_display = ('id', 'interfacename','interface_desc', 'create_time')
    # list_per_page = 20