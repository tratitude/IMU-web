from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import user_detail
admin.site.register(user_detail)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
"""class accountInline(admin.StackedInline):
    model = user_detail
    can_delete = False
    verbose_name_plural = 'user_detail'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (accountInline, )
# Register your models here.
"""

