from django.urls import path
from .views import deleteTodo, index, about, login, register, logout

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('delete-todo/<int:id>/', deleteTodo, name="deleteTodo"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
]
