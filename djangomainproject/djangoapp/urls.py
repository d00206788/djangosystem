from django.urls import path
from . import views
from djangoapp.views import ChangePasswordView

urlpatterns = [
    path('', views.home, name="home"),
    path('breeds/', views.breeds, name="breeds"),
    path('create_dog/', views.createDog, name="create_dog"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.profile, name="user-page"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
