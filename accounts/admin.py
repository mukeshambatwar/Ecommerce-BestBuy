from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','first_name','last_name')      # It creates link
    readonly_fields = ('last_login','date_joined')               # It read only fields
    ordering = ('-date_joined',)                                 # It displays in descending order


    filter_horizontal = ()      # It shows all fields in horizontal 
    list_filter = ()            #
    fieldsets = ()              # make password read-only

admin.site.register(Account, AccountAdmin)