from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = "routes"),
    path('notes/', views.getNotes, name = "notes"),
    # path('notes/create/', views.createNote, name = "create_note"),
    # path('notes/<str:pk>/update/', views.updateNote, name = "update_note"),
    # path('notes/<str:pk>/delete/', views.deleteNote, name = "delete_note"),
    path('notes/<str:pk>/', views.getNote, name = "note")
]