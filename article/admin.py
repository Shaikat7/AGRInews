from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

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
from .models import Time_sensitive
from .models import Not_Time_sensitive


# Register your models here.
class NewsArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

class GovernmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class WeatherAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
    
class InternationalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class EconomicAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Animal_HUsbandryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Crop_Diseases_and_ProtectionsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Technologies_and_MethodsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class OtherAgriNewsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Positive_sentimentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Negative_sentimentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Time_sensitiveAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

class Not_Time_sensitiveAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...





admin.site.register(NewsArticles,NewsArticleAdmin)
admin.site.register(Government,GovernmentAdmin)
admin.site.register(Weather,WeatherAdmin)
admin.site.register(International,InternationalAdmin)
admin.site.register(Economic,EconomicAdmin)
admin.site.register(Animal_Husbandry,Animal_HUsbandryAdmin)
admin.site.register(Crop_Diseases_and_Protections,Crop_Diseases_and_ProtectionsAdmin)
admin.site.register(Technologies_and_Methods,Technologies_and_MethodsAdmin)
admin.site.register(OtherAgriNews,OtherAgriNewsAdmin)
admin.site.register(Positive_sentiment,Positive_sentimentAdmin)
admin.site.register(Negative_sentiment,Negative_sentimentAdmin)
admin.site.register(Time_sensitive,Time_sensitiveAdmin)
admin.site.register(Not_Time_sensitive,Not_Time_sensitiveAdmin)


