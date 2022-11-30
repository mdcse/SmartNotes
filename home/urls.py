from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    # path('authorized/', views.authorized, name='authorized'),
    path('authorized/', views.AuthorizedView.as_view(), name='authorized'),
]