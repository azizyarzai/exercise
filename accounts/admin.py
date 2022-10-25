from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from accounts.models import Account


class AccountAdmin(BaseUserAdmin):
    fieldsets = [
        ("Personal Info", {"fields": ["email", 'password', 'date_of_birth',
         'name', 'role', 'is_superuser', 'is_active', 'is_staff']}),
        ("User Permission", {'fields': ["user_permissions", 'groups']})
    ]

    add_fieldsets = [
        (None, {"fields": [
            "email", 'role', 'name', "password1",
            "password2",
        ]})
    ]
    list_display = ["name", "email", "role"]
    ordering = ['name']


admin.site.register(Account, AccountAdmin)
