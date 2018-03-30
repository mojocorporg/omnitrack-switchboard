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


class FleetOwnerAdmin(admin.ModelAdmin):
    list_display = ["fleet_owner", "phone"]
    list_filter = ["fleet_owner__is_active"]
    search_fields = ["fleet_owner__username"]


class OperationAdmin(admin.ModelAdmin):
    list_display = ["operation_user", "source", "destination"]
    search_fields = ["operation_user__username"]


class FeedAdmin(admin.ModelAdmin):
    list_display = ["vehicle", "city"]
    search_fields = ["vehicle__registration_number"]


class VehicleAdmin(admin.ModelAdmin):
    list_display = ["registration_number", "fleet_owner", "brand", "model", "fuel_type", "color", "vehicle_type"]
    list_filter = ["color", "fuel_type"]
    search_fields = ["registration_number"]


class LeadAdmin(admin.ModelAdmin):
    list_display = ["commission_agent", "source", "destination", "departure_date", "vehicle_type", "material_to_carried"]
    list_filter = ["departure_date", "material_to_carried"]


class QuoteAdmin(admin.ModelAdmin):
    list_display = ["lead", "commission_agent", "vehicle", "price", "currency", "etd"]
    search_fields = ["vehicle__registration_number", "commission_agent__agent__username"]


class JobAdmin(admin.ModelAdmin):
    list_display = ["quote", "title", "delivery_date", "status"]
    list_filter = ["status", "delivery_date"]


class RatingAdmin(admin.ModelAdmin):
    list_display = ["job", "rated_entity", "rating"]
    list_filter = ["rating", "rated_entity"]


admin.site.register(FleetOwner, FleetOwnerAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(JobStatus)
admin.site.register(Job, JobAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(MaterialType, MaterialTypeAdmin)
