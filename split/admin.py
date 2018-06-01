from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(GroupProfile)
admin.site.register(ExpenseDetail)