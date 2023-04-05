from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Bettor
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Bettor
    list_display =('email', 'number', 'is_active', 'is_staff')
    list_filter = ("email", "is_staff", "is_active",)
    
    fieldsets = (
        (None, {"fields": ("email","number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "number" ,"password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email","number",)
    ordering = ("email",)


# Register your models here.
admin.site.register(Bettor, CustomUserAdmin,)