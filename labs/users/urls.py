from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('add-book/', views.add_new_book, name='add-book'),
    path('<int:id>/', views.get_user_books, name='get-user-books')
]
