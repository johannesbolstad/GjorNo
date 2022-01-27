from django.contrib import admin

# Register your models here.
from .models import Activity, OrgUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Velge hvilke felt som skal vises i Users
#
#class UserAdmin2(admin.ModelAdmin):
#    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser')
#    list_filter = ('is_staff', 'is_superuser')
#admin.site.unregister(User)
#admin.site.register(User, UserAdmin2)


# Velge hvilke felt som vises i OrgUser
class OrgUserAdmin(admin.ModelAdmin):
    list_display = ('org_name',)

admin.site.register(Activity)
admin.site.register(OrgUser, OrgUserAdmin)


