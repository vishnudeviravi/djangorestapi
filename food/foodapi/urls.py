from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.FoodList.as_view()),

]
