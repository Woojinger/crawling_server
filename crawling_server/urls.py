from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

class HomeTemplateView(TemplateView) :
    template_name = "index.html"

urlpatterns = [
    path('', include('server.urls')),
    path('admin/', admin.site.urls),
]
