from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

class UserModelAdmin(UserAdmin):
    model = User
    list_display = ["id", "name", "email", "is_active", "is_staff", "is_customer", "is_seller", "is_superuser"]
    list_filter = ["is_superuser", "is_customer", "is_seller", "name"]  # Added name to filter

    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal Information", {"fields": ["name", "city"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "is_customer", "is_seller"]}),
        ("Extra Info", {"fields": ["date_of_birth", "gender"]}),
    ]

    add_fieldsets = [
        (None, {
            'classes': ('wide',),  # Makes the form wide
            'fields': ("email", "password1", "password2", "name", "city", 
                       "is_active", "is_staff", "is_superuser", "is_customer", "is_seller")
        }),
    ]

    search_fields = ["email", "name"]
    ordering = ["id"]

    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(User, UserModelAdmin)
