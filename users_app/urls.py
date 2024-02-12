from django.urls import path,include
from users_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.register,name='register' ),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',views.logout_view,name='logout')
]