from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('amazon/<str:q>/select/', views.AmazonSelect, name="select"),
    path('amazon/<str:q>/', views.AmazonList.as_view()),
]
