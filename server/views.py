from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gevolution, Amazon
from .serializers import AmazonSerializer, GevolutionSerializer
from django.views.generic import ListView
from rest_framework import viewsets
from datetime import date



def index(request):
    return render(
        request,
        "server/index.html"
    )

def AmazonSelect(request, q):
    context = {"Category" : q}
    if (q == "Bedroom Furniture"):
        context['Parent_Category'] = "Furniture"
    elif ((q == "Beds, Frames & Bases") or (q == "Bedroom Armoires") or (q == "Mattresses & Box Springs")):
        context['Parent_Category'] = "Bedroom Furniture"
    elif ((q == "Bases & Foundations") or (q == "Bed Frames") or (q == "Beds") or (q == "Headboards & Footboards")):
        context['Parent_Category'] = "Beds, Frames & Bases"
    else:
        context['Parent_Category'] = "Mattresses & Box Springs"
    return render(
        request,
        "server/amazon_select.html",
        context
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
        date = self.request.GET.get("date")
        datelist = date.split("-")
        y = datelist[0]
        realdate = y[2:] + "/" + datelist[1] + "/" + datelist[2]
        object_list = Amazon.objects.filter(Selected_category=q, Date=realdate)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AmazonList, self).get_context_data()
        q = self.kwargs['q']
        date = self.request.GET.get("date")
        datelist = date.split("-")
        y = datelist[0]
        realdate = y[2:] + "/" + datelist[1] + "/" + datelist[2]
        if(q == "Bedroom Furniture") :
            context['Parent_Category'] = "Furniture"
        elif ((q == "Beds, Frames & Bases")or(q == "Bedroom Armoires")or(q=="Mattresses & Box Springs")):
            context['Parent_Category'] = "Bedroom Furniture"
        elif ((q == "Bases & Foundations")or(q == "Bed Frames")or(q=="Beds")or(q=="Headboards & Footboards")):
            context['Parent_Category'] = "Beds, Frames & Bases"
        else :
            context['Parent_Category'] = "Mattresses & Box Springs"
        context['Category'] = "{}".format(q)

        context['Date'] = realdate
        return context
