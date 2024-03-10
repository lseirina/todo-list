"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for user."""
    ordering = ['id']
    list_display = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email',)}),
        (
            ('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
                }
        ),
        (('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    readonly_fields = ['last_login', 'date_joined']

if admin.site.is_registered(User):
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(models.Task)




