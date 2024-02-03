from django.urls import path
from . import views
from .views import appointment_list, create_appointment, edit_appointment, delete_appointment


urlpatterns = [
    path ('', views.home_page, name="homepage"),
    path ('about/', views.about_page, name="aboutPage"),
    path ('login/', views.login_page, name="loginPage"),
    path ('contact/', views.contact_page, name="contactPage"),
    path ('service/', views.service_page, name="servicePage"),
    path ('home/', views.home_page, name="homePage"),
    path ('register/', views.register_page, name="registerPage"),
    path('logout_user', views.logout_user, name="logout" ),
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/create/', create_appointment, name='create_appointment'),
    path('appointments/edit/<int:pk>/', edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', delete_appointment, name='delete_appointment'),

]