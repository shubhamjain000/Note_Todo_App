from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Optional landing page
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/edit/<int:id>/', views.edit_note, name='edit_note'),
    path('notes/delete/<int:id>/', views.delete_note, name='delete_note'),

    path('todos/', views.todo_list, name='todo_list'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('todos/delete/<int:id>/', views.delete_todo, name='delete_todo'),
]
