"""
URL configuration for Agrinews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import (news_article_view,gov_article_view,OtherAgriNews_article_view,Animal_Husbandry_article_view,
                Crop_Diseases_and_Protections_article_view,Economic_article_view,weather_article_view,
                International_article_view,Technologies_and_Methods_article_view, Positive_sentiment_article_view, 
                Negative_sentiment_article_view, Time_sensitive_article_view, Not_Time_sensitive_article_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_article_view,name='home'),
    path('all-news/', OtherAgriNews_article_view,name='all-news'),
    path('animal-husbandry/', Animal_Husbandry_article_view,name='animal-husbandry'),
    path('crop/', Crop_Diseases_and_Protections_article_view,name='crop'),
    path('economic-agri/', Economic_article_view,name='economic-agri'),
    path('environment/', weather_article_view,name='environment'),
    path('government/', gov_article_view,name='government'),
    path('international-agri', International_article_view,name='international-agri'),
    path('agri-technology', Technologies_and_Methods_article_view,name='agri-technology'),
    path('positive-agri', Positive_sentiment_article_view,name='positive-agri'),
    path('negative-agri', Negative_sentiment_article_view,name='negative-agri'),
    path('time-sensitive-agri', Time_sensitive_article_view,name='time-sensitive-agri'),
    path('not-time-sensitive-agri', Not_Time_sensitive_article_view,name='not-time-sensitive-agri'),
]
