from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    # URL for viewing all spaces
    path('', lambda request: redirect('venue:space_list'), name='venue_home'),
    path('space_list/', views.space_list, name='space_list'),
    path('toggle/<int:space_id>/', views.toggle_booking, name='toggle_booking'),
    path('book/<int:space_id>/', views.book_space, name='book_space'),
]
