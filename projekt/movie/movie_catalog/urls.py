from django.urls import path
import movies.views as views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.movie_create, name='movie_create'),
    path('edit/<int:pk>/', views.movie_edit, name='movie_edit'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

]