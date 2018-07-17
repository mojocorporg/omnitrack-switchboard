from django.contrib import admin
from .models import CommissionAgent

# Register your models here.
class CommissionAgentAdmin(admin.ModelAdmin):
    list_display = ["agent", "company_name", "phone"]
    search_fields = ["agent__username"]
    list_filter = ["agent__is_active"]
    filter_horizontal = ("hub",)

admin.site.register(CommissionAgent, CommissionAgentAdmin)
