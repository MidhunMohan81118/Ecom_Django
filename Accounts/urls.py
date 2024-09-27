from django.urls import path
from . import views

urlpatterns = [
    #home page
    path('', views.dashboard, name='dashboard'),
    path('register/',views.register,name='user_registration'),
    path('login/',views.login,name='user_login'),
    path('logout/',views.logout,name='user_logout'),
    #email activation
    path('activate/<uidb64>/<token>/',views.activate,name='user_activation'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('forgotpassword/',views.forgot_password, name="forgot_password"),
    path('resetpassword/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    path('resetpassword/',views.reset_password, name="reset_password"),
]
