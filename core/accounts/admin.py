from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'created_date', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('created_date', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('created_date',)
    ordering = ('-created_date',)
    fieldsets = (
        ('Authentication', {'fields':('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',)}),
        ('Group permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important date', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
        }),
    
    )

admin.site.register(User, CustomUserAdmin)
