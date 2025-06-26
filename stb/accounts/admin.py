from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'gender', 'dob', 'phone_number', 'email')
    search_fields = ('student_id', 'student_name', 'email')
    list_filter = ('gender',)