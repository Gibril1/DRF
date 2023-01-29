from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'username', 'last_name')
    # ordering = ('-start_date')
    list_filter = ('email', 'first_name', 'id')
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
    )

    fieldsets = (
        (None, { 'fields': ('email', 'username', 'first_name', 'last_name', 'roles', 'password')}),
        ('Permissions', { 'fields': ('is_staff', 'is_active', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields': ('first_name', 'last_name', 'email', 'password', 'password2', 'roles', 'username')
        }
        )
    )
admin.site.register(User, UserAdmin)
