from django.contrib import admin
from .models import City, State, Country, Currency

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        "name", "code", "is_active"
    ]
    list_filter = ["is_active"]


class StateAdmin(admin.ModelAdmin):
    list_display = [
        "name", "code", "country", "is_active"
    ]
    list_filter = ["is_active"]


class CityAdmin(admin.ModelAdmin):
    list_display = [
        "name", "state", "is_active"
    ]
    list_filter = ["is_active"]


class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "name", "symbol", "is_active"
    ]
    list_filter = ["is_active"]

admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Currency, CurrencyAdmin)
