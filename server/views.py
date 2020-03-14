from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gevolution, Amazon
from .serializers import AmazonSerializer, GevolutionSerializer
from django.views.generic import ListView
from rest_framework import viewsets


def index(request):
    return render(
        request,
        "server/index.html"
    )

class AmazonView(viewsets.ModelViewSet):
	serializer_class = AmazonSerializer
	def get_queryset(self):
		queryset = Amazon.objects.all()
		return queryset

class GevolutionView(viewsets.ModelViewSet):
	serializer_class = GevolutionSerializer
	def get_queryset(self):
		queryset = Gevolution.objects.all()
		return queryset

class AmazonList(ListView):
    model = Amazon
    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Amazon.objects.filter(Selected_category=q)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AmazonList, self).get_context_data()
        context['Category'] = 'Category: "{}"'.format(self.kwargs['q'])
        return context
