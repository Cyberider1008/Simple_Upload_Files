from django.utils.html import format_html
from django.contrib import admin
from app1.models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    
    model = Employee
    list_display = ['name', 'email', 'desc', 'document', 'uploaded_at']
    search_fields = ['name', 'email', 'desc', 'document', 'uploaded_at']


# admin.site.register(Employee, EmployeeAdmin)