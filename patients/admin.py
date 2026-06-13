from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'gender', 'phone', 'created_by', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
