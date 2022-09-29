from django.contrib import admin
from .models.User import User
from .models.Account import Account
from .models.Rol import Rol

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Rol)