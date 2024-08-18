from django.contrib import admin

import authuser
from authuser.models import User

# Register your models here.

admin.site.register(User)
