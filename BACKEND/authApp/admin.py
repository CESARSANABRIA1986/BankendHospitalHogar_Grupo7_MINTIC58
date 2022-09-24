from django.contrib import admin
from .models.User import User
from .models.Account import Account

admin.site.register(User)
admin.site.register(Account)