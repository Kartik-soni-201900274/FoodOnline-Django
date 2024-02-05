from django.contrib import admin

from accounts.models import User, UserProfile

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ()
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = ()  # add the fields you want to display here
    ordering = ('-date_joined',)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

# Register your models here.
