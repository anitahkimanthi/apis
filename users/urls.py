from django.urls import path
from .views import register, login, get_users,delete_user



# urlpatterns - an array containing urls
urlpatterns=[
    path('register', register, name='register'),
    path('login', login, name='login'),  
    path('users', get_users),
    path('users/delete/<int:user_id>', delete_user, name='delete_user'),  # ✅ DELETE route

]