from django.contrib import admin
from .models import Employee

# Slide 17: Django Admin Panel Demo
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'salary', 'created_at')  # type: ignore
    search_fields = ('name', 'email', 'department')
    list_filter = ('department', 'created_at')
    ordering = ('-created_at',)
