from django.urls import path
from Main_App import views
urlpatterns = [
    path('', views.index, name="index"),
    path('abaut/', views.abaut, name="abaut"),
    
]
