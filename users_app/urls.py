from django.urls import path
from . import views

urlpatterns = [
    path("home",views.index, name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("login&reg",views.login_reg,name="login&reg"),
    path("logout",views.logout,name="logout"),

    path("book",views.book_appointment,name="book_appointment"),
    path("create_appointment",views.create_appointment,name="create_appointment"),
    
    path("book/select-service",views.select_service,name="select_service"),
    
    path("book/finalize",views.finalize_appointment,name="finalize"),
    path("book/complete",views.complete_appointment,name="complete"),
    path("services",views.services,name="services"),
    path("about",views.about,name="about"),
]