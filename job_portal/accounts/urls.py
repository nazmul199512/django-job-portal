from django.urls import path
from .views import signup, employee_login, logout_view

app_name = 'accounts'

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('login/', employee_login, name='login'),
    path('logout/', logout_view, name='logout'),


]
