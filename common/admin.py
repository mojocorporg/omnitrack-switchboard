from django.contrib import admin
from .models import City, State, Country, Vehicle

# Register your models here.
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Vehicle)
