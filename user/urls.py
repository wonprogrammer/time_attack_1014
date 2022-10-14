from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),

    # path('<str:username>/', views.home, name='home'),
]