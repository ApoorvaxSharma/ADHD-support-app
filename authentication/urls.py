from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.signIn),
	path('postsignIn/', views.postsignIn),
	path('signUp/', views.signUp, name="signup"),
	path('logout/', views.logout, name="log"),
	path('postsignUp/', views.postsignUp),
]
