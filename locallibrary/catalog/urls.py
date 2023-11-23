from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.template.context_processors import static

from . import views
from .views import user_login, create_design_request, view_own_requests, delete_design_request, change_status, \
    add_category, manage_categories
from .views import register
from .views import user_logout
from .views import home
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]