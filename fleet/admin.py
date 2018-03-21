from django.contrib import admin
from .models import *

# Register your models here.
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name", "is_active"
    ]
    list_filter = ["is_active"]


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = [
        "type", "length", "weight"
    ]
    list_filter = ["type"]


admin.site.register(FleetOwner)
admin.site.register(Operation)
admin.site.register(Feed)
admin.site.register(Vehicle)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Lead)
admin.site.register(Quote)
admin.site.register(Job)
admin.site.register(Rating)
admin.site.register(MaterialType, MaterialTypeAdmin)
