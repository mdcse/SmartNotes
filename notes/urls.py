from django.urls import path

from notes import views

urlpatterns = [
    path('notes', views.NotesListViews.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NotesDetailViews.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit', views.NotesUpdateViews.as_view(), name='notes.update'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
]