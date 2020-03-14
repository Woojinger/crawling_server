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
    paginate_by = 50
    def get_queryset(self):
        q = self.kwargs['q']
        y = self.kwargs['y']
        m = self.kwargs['m']
        d = self.kwargs['d']
        date=y+"/"+m+"/"+d
        object_list = Amazon.objects.filter(Selected_category=q, Date=date)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AmazonList, self).get_context_data()
        q = self.kwargs['q']
        y = self.kwargs['y']
        m = self.kwargs['m']
        d = self.kwargs['d']
        date = y + "/" + m + "/" + d
        object= Amazon.objects.filter(Selected_category=q, Date=date)[0]
        context['Category'] = "{}".format(q)
        context['Parent_Category'] = object.Parent_category
        context['Date'] = date
        return context
