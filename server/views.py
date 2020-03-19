from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gevolution, Amazon, Fiftytohundred
from .serializers import AmazonSerializer, GevolutionSerializer, FiftytohundredSerializer
from django.views.generic import ListView
from rest_framework import viewsets
from django.db.models import Q
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

class AmazonbrandList(ListView):
    model = Amazon
    template_name = 'server/amazonbrand_list.html'
    def get_queryset(self):
        q = self.kwargs['q']
        brand = self.kwargs['brand']
        if(brand=="Linenspa") :
            preobject_list = Amazon.objects.filter(Selected_category=q)
            object_list = preobject_list.filter(Q(Brand="Linenspa") | Q(Brand="LINENSPA"))
        else :
            object_list = Amazon.objects.filter(Selected_category=q, Brand=brand)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AmazonbrandList, self).get_context_data()
        q = self.kwargs['q']
        context['Category'] = "{}".format(q)
        brand = self.kwargs['brand']
        context['Brand'] = brand
        if (brand == "Linenspa"):
            preobject_list = Amazon.objects.filter(Selected_category=q)
            object_list = preobject_list.filter(Q(Brand="Linenspa") | Q(Brand="LINENSPA"))
        elif (brand == "LUCID"):
            preobject_list = Amazon.objects.filter(Selected_category=q)
            object_list = preobject_list.filter(Q(Brand="Lucid") | Q(Brand="LUCID"))
        else:
            object_list = Amazon.objects.filter(Selected_category=q, Brand=brand)
        dictionary100 = {}
        hundredrank = Fiftytohundred.objects.filter(Selected_category=q)
        if (brand == "Zinus") :
            for item in hundredrank :
                dictionary100[item.Date] = item.Zinus
        if (brand == "Sleep") :
            for item in hundredrank :
                dictionary100[item.Date] = item.Sleep
        if (brand == "LUCID") :
            for item in hundredrank :
                dictionary100[item.Date] = item.bigLUCID +item.Lucid
        if (brand == "Linenspa") :
            for item in hundredrank :
                dictionary100[item.Date] = item.bigLINENSPA + item.Linenspa
        if (brand == "AmazonBasics") :
            for item in hundredrank :
                dictionary100[item.Date] = item.AmazonBasics
        if (brand == "Casper") :
            for item in hundredrank :
                dictionary100[item.Date] = item.Casper
        dictionary50 = {}
        dictionary20 = {}
        dictionary5 = {}
        for item in object_list:
            itemdate = item.Date
            if itemdate in dictionary100 :
                dictionary100[itemdate] = dictionary100[itemdate] + 1
            if itemdate in dictionary50:
                dictionary50[itemdate] = dictionary50[itemdate] + 1
            else :
                dictionary50[itemdate] = 1
                dictionary20[itemdate] = 0
                dictionary5[itemdate] = 0
            if int(item.Rank)<21:
                if itemdate in dictionary20 :
                    dictionary20[itemdate] = dictionary20[itemdate] + 1
            if int(item.Rank)<6:
                if itemdate in dictionary5 :
                    dictionary5[itemdate] = dictionary5[itemdate] + 1


        brandarray100 = [["Date", brand]]
        brandarray50 = [["Date", brand]]
        brandarray20 = [["Date", brand]]
        brandarray5 = [["Date", brand]]
        for key in dictionary50.keys():
            if key in dictionary100.keys() :
                column100 = [key, dictionary100[key]]
                brandarray100.append(column100)
            column50 = [key, dictionary50[key]]
            column20 = [key, dictionary20[key]]
            column5 = [key, dictionary5[key]]
            brandarray50.append(column50)
            brandarray20.append(column20)
            brandarray5.append(column5)
        context['arr100'] = brandarray100
        context['arr50'] = brandarray50
        context['arr20'] = brandarray20
        context['arr5'] = brandarray5
        if(len(brandarray100)==1) :
            context["hundred"] = False
        else :
            context["hundred"] = True
        return context


class AmazonOtherBrand(ListView):
    model = Amazon
    template_name = 'server/amazonbrand_list.html'
    def get_queryset(self):
        q = self.kwargs['q']
        brand = self.request.GET.get("brand")
        object_list = Amazon.objects.filter(Selected_category=q, Brand=brand)
        return object_list
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AmazonOtherBrand, self).get_context_data()
        q = self.kwargs['q']
        context['Category'] = "{}".format(q)
        brand = self.request.GET.get("brand")
        context['Brand'] = brand
        if ((brand == "Linenspa") or (brand == "LINENSPA")):
            preobject_list = Amazon.objects.filter(Selected_category=q)
            object_list = preobject_list.filter(Q(Brand="Linenspa") | Q(Brand="LINENSPA"))
        elif ((brand == "Lucid") or (brand == "LUCID")):
            preobject_list = Amazon.objects.filter(Selected_category=q)
            object_list = preobject_list.filter(Q(Brand="Lucid") | Q(Brand="LUCID"))
        else:
            object_list = Amazon.objects.filter(Selected_category=q, Brand=brand)
        dictionary50 = {}
        dictionary20 = {}
        dictionary5 = {}
        for item in object_list:
            itemdate = item.Date
            if itemdate in dictionary50:
                dictionary50[itemdate] = dictionary50[itemdate] + 1
            else:
                dictionary50[itemdate] = 1
                dictionary20[itemdate] = 0
                dictionary5[itemdate] = 0
            if int(item.Rank) < 21:
                if itemdate in dictionary20:
                    dictionary20[itemdate] = dictionary20[itemdate] + 1
            if int(item.Rank) < 6:
                if itemdate in dictionary5:
                    dictionary5[itemdate] = dictionary5[itemdate] + 1
        brandarray50 = [["Date", brand]]
        brandarray20 = [["Date", brand]]
        brandarray5 = [["Date", brand]]
        for key in dictionary50.keys():
            column50 = [key, dictionary50[key]]
            column20 = [key, dictionary20[key]]
            column5 = [key, dictionary5[key]]
            brandarray50.append(column50)
            brandarray20.append(column20)
            brandarray5.append(column5)
        context['arr50'] = brandarray50
        context['arr20'] = brandarray20
        context['arr5'] = brandarray5
        context["hundred"] = False

        return context

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

class FiftytohundredView(viewsets.ModelViewSet):
    serializer_class = FiftytohundredSerializer
    def get_queryset(self):
        queryset = Fiftytohundred.objects.all()
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

def GevolutionStart(request, q):
    context = {"Appmarket": q}
    return render(
        request,
        "server/gevolution_start.html",
        context
    )
class GevolutionList(ListView):
    model = Gevolution
    template_name = 'server/gevolution_select.html'
    def get_queryset(self):
        q = self.kwargs['q']
        date = self.request.GET.get("date")
        datelist = date.split("-")
        y = datelist[0]
        realdate = y[2:] + "/" + datelist[1] + "/" + datelist[2]
        preobject_list = Gevolution.objects.filter(Date=realdate)
        if(q=="Aos") :
            object_list = preobject_list.filter(Q(Category="AosKorFree") | Q(Category="AosKorCharge") | Q(Category="AosKorSales"))
        elif (q == "Ios"):
            object_list = preobject_list.filter(
                Q(Category="IosKorFree") | Q(Category="IosKorCharge") | Q(Category="IosKorSales"))
        else :
            object_list = []
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GevolutionList, self).get_context_data()
        q = self.kwargs['q']
        date = self.request.GET.get("date")
        datelist = date.split("-")
        y = datelist[0]
        realdate = y[2:] + "/" + datelist[1] + "/" + datelist[2]
        context['Appmarket'] = "{}".format(q)
        context['Date'] = realdate
        return context

class GevolutionGraph(ListView):
    model = Gevolution
    template_name = 'server/gevolutionbrand_graph.html'
    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = Gevolution.objects.filter(Name=name)
        return object_list
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GevolutionGraph, self).get_context_data()
        name = self.request.GET.get("name")
        context['Name'] = name
        object_list = Gevolution.objects.filter(Name=name)
        AosFree_list = object_list.filter(Category="AosKorFree")
        AosCharge_list = object_list.filter(Category="AosKorCharge")
        AosSales_list = object_list.filter(Category="AosKorSales")
        IosFree_list = object_list.filter(Category="IosKorFree")
        IosCharge_list = object_list.filter(Category="IosKorCharge")
        IosSales_list = object_list.filter(Category="IosKorSales")
        dicAosFree = {}
        dicAosCh = {}
        dicAosSales = {}
        dicIosFree = {}
        dicIosCh = {}
        dicIosSales = {}
        if(len(AosFree_list)!=0) :
            context["AF"] = True
        if (len(AosCharge_list) != 0):
            context["AC"] = True
        if (len(AosSales_list) != 0):
            context["AS"] = True
        if (len(IosFree_list) != 0):
            context["IF"] = True
        if (len(IosCharge_list) != 0):
            context["IC"] = True
        if (len(IosSales_list) != 0):
            context["IS"] = True

        for item in AosFree_list:
            itemdate = item.Date
            dicAosFree[itemdate] = item.Rank
        for item in AosCharge_list:
            itemdate = item.Date
            dicAosCh[itemdate] = item.Rank
        for item in AosSales_list:
            itemdate = item.Date
            dicAosSales[itemdate] = item.Rank
        for item in IosFree_list:
            itemdate = item.Date
            dicIosFree[itemdate] = item.Rank
        for item in IosCharge_list:
            itemdate = item.Date
            dicIosCh[itemdate] = item.Rank
        for item in IosSales_list:
            itemdate = item.Date
            dicIosSales[itemdate] = item.Rank

        AosFree = [["Date", "Rank"]]
        AosCharge = [["Date", "Rank"]]
        AosSales = [["Date", "Rank"]]
        IosFree = [["Date", "Rank"]]
        IosCharge = [["Date", "Rank"]]
        IosSales = [["Date", "Rank"]]

        for key in dicAosFree.keys():
            AosF = [key, int(dicAosFree[key])]
            AosFree.append(AosF)
        for key in dicAosCh.keys():
            AosCh = [key, int(dicAosCh[key])]
            AosCharge.append(AosCh)
        for key in dicAosSales.keys():
            AosS = [key, int(dicAosSales[key])]
            AosSales.append(AosS)
        for key in dicIosFree.keys():
            IosF = [key, int(dicIosFree[key])]
            IosFree.append(IosF)
        for key in dicIosCh.keys():
            IosCh = [key, int(dicIosCh[key])]
            IosCharge.append(IosCh)
        for key in dicIosSales.keys():
            IosS = [key, int(dicIosSales[key])]
            IosSales.append(IosS)
        context['AosFree'] = AosFree
        context['AosCharge'] = AosCharge
        context['AosSales'] = AosSales
        context['IosFree'] = IosFree
        context['IosCharge'] = IosCharge
        context['IosSales'] = IosSales

        return context