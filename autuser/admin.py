from django.contrib import admin

import autuser
from autuser.models import User

# Register your models here.

admin.site.register(User)
