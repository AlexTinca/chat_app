from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages_post),
    path('messages/<str:room_id>/', views.messages_get),
    path('group_chat/', views.room_post),
    path('group_chat/<str:room_id>/participants/', views.participant_post),
    path('group_chat/<str:room_id>/participants/<str:user_id>/', views.participant_delete),
]