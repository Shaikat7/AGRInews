from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView,DetailView
from .models import NewsArticles
from .models import Government
from .models import Weather
from .models import International
from .models import Economic
from .models import Animal_Husbandry
from .models import Crop_Diseases_and_Protections
from .models import Technologies_and_Methods
from .models import OtherAgriNews
from .models import Positive_sentiment
from .models import Negative_sentiment
from .models import Not_Time_sensitive
from .models import Time_sensitive

# Create your views here.
# class NewsArticleView(ListView):
#     model = NewsArticles
#     template_name = "index2.html"
#     ordering = ['-id']

def news_article_view(request):
    if request.method == "GET":
        query = request.GET.get("q")
        submitbtn = request.GET.get("submit")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = NewsArticles.objects.filter(lookups).distinct()
            print("news")
        else:
            news = NewsArticles.objects.all().order_by('-id')[:20]
    gov =  Government.objects.all().order_by('-id')[:2]
    env =  Weather.objects.all().order_by('-id')[:2]
    inter =  International.objects.all().order_by('-id')[:2]
    anim =  Animal_Husbandry.objects.all().order_by('-id')[:2]
    eco =  Economic.objects.all().order_by('-id')[:2]
    cro =  Crop_Diseases_and_Protections.objects.all().order_by('-id')[:2]
    tech =  Technologies_and_Methods.objects.all().order_by('-id')[:2]
    all =  OtherAgriNews.objects.all().order_by('-id')[:2]
    pos =  Positive_sentiment.objects.all().order_by('-id')[:2]
    neg =  Negative_sentiment.objects.all().order_by('-id')[:2]
    nt =  Not_Time_sensitive.objects.all().order_by('-id')[:2]
    ti =  Time_sensitive.objects.all().order_by('-id')[:2]
    context = {
        'news_list': news,
        'gov' : gov,
        'env' : env,
        'inter': inter,
        'anim' : anim,
        'cro' : cro,
        'tech' : tech,
        'all' : all,
        'pos' : pos,
        'neg' : neg,
        'nt' : nt,
        'ti' : ti,
        'eco' : eco
    }
    return render(request, 'index2.html', context)


def gov_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Government.objects.filter(lookups).distinct()
        else:
            news =  Government.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Government & Subsidy Related News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def weather_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Weather.objects.filter(lookups).distinct()
        else:
            news =  Weather.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Environment Related News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def International_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = International.objects.filter(lookups).distinct()
        else:
            news =  International.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "International Agriculture News",
        'news_list': news
    }
    return render(request, 'gov.html', context)
    

def Animal_Husbandry_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Animal_Husbandry.objects.filter(lookups).distinct()
        else:
            news =  Animal_Husbandry.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Animal Husbandry News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Economic_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Economic.objects.filter(lookups).distinct()
        else:
            news =  Economic.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Agriculture Economic News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Crop_Diseases_and_Protections_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Crop_Diseases_and_Protections.objects.filter(lookups).distinct()
        else:
            news =  Crop_Diseases_and_Protections.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Crop Diseases and Protections News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Technologies_and_Methods_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Technologies_and_Methods.objects.filter(lookups).distinct()
        else:
            news =  Technologies_and_Methods.objects.all().order_by('-id')[:30]
    context = {
        'heading' : "Technologies and Methods",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def OtherAgriNews_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = OtherAgriNews.objects.filter(lookups).distinct()
        else:
            news =  OtherAgriNews.objects.all().order_by('-id')[:40]
    context = {
        'heading' : "All News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Positive_sentiment_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Positive_sentiment.objects.filter(lookups).distinct()
        else:
            news =  Positive_sentiment.objects.all().order_by('-id')[:15]
    context = {
        'heading' : "Positive Agriculture News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Negative_sentiment_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Negative_sentiment.objects.filter(lookups).distinct()
        else:
            news =  Negative_sentiment.objects.all().order_by('-id')[:15]
    context = {
        'heading' : "Negative Agriculture News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

def Not_Time_sensitive_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Not_Time_sensitive.objects.filter(lookups).distinct()
        else:
            news =  Not_Time_sensitive.objects.all().order_by('id')[:30]
    context = {
        'heading' : "Not Time Sensitive News",
        'news_list': news
    }
    return render(request, 'gov.html', context)
def Time_sensitive_article_view(request):
    if request.method == "GET":
        print("ingov")
        query = request.GET.get("q")
        if query is not None:
            lookups = Q(title__icontains=query)
            news = Time_sensitive.objects.filter(lookups).distinct()
        else:
            news =  Time_sensitive.objects.all().order_by('-id')[:10]
    context = {
        'heading' : "Time Sensitive News",
        'news_list': news
    }
    return render(request, 'gov.html', context)

