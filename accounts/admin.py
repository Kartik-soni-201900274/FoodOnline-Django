from django.contrib import admin

from accounts.models import User, UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    readonly_fields = ("password",)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

# Register your models here.
