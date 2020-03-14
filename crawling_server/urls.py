from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from server import views
from rest_framework import routers


class HomeTemplateView(TemplateView) :
    template_name = "index.html"

router = routers.DefaultRouter()
router.register('amazon', views.AmazonView, 'amazon')
router.register('gevolution', views.GevolutionView, 'gevolution')

urlpatterns = [
    path('', include('server.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
