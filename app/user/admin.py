from django.contrib import admin
from .models import User, VipUser, VipUserManager

# Register your models here.
admin.site.register(User)
# admin.site.register(VipUserManager)
admin.site.register(VipUser)