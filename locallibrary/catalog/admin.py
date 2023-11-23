from django.core.exceptions import ValidationError

from .forms import ApplicationCheckForm
from .models import CustomUser
from .models import DesignRequest
from .models import Category
from django.contrib import admin

admin.site.register(CustomUser)
admin.site.register(Category)


from django.contrib import admin


