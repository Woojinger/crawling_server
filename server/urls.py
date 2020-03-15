from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('amazon/<str:q>/select/', views.AmazonSelect, name="select"),
    path('amazon/<str:q>/graph/<str:brand>', views.AmazonbrandList.as_view()),
    path('amazon/<str:q>/graph/', views.AmazonOtherBrand.as_view()),
    path('amazon/<str:q>/', views.AmazonList.as_view()),
    path('gevolution/<str:q>/select',views.GevolutionStart),
    path('gevolution/graph/', views.GevolutionGraph.as_view()),
    path('gevolution/<str:q>/', views.GevolutionList.as_view()),
]
