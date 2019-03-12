# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
class TransporterAdmin(admin.ModelAdmin):
    list_display = ["transporter", "phone"]
    list_filter = ["transporter__is_active"]
    search_fields = ["transporter__username"]

admin.site.register(Transporter, TransporterAdmin)
