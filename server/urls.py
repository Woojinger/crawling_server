from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amazon/<str:q>/<str:y>/<str:m>/<str:d>/', views.AmazonList.as_view()),
]