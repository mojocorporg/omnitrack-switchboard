from django.contrib import admin
from .models import CommissionAgent

# Register your models here.
class CommissionAgentAdmin(admin.ModelAdmin):
    list_display = ["agent", "company_data", "phone", "hub"]
    search_fields = ["agent__username"]
    list_filter = ["agent__is_active"]

admin.site.register(CommissionAgent, CommissionAgentAdmin)
