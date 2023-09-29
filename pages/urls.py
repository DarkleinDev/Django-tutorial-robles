from django.urls import path
from pages import views
urlpatterns = [
    path('pagina/<str:slug>/', views.page, name="page")
]
