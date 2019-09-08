from django.contrib import admin
from employees.models import User


class UserModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserModelAdmin)
