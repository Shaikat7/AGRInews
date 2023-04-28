from django.db import models
from django.utils.text import slugify

# Create your models here.

class NewsArticles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "NewsArticle"
        verbose_name_plural = "NewsArticles"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(NewsArticles,self).save(*args,**kwargs)

class Government(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Government"
        verbose_name_plural = "Governments"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Government,self).save(*args,**kwargs)

class Weather(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Weather"
        verbose_name_plural = "Weathers"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Weather,self).save(*args,**kwargs)

class International(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "International"
        verbose_name_plural = "Internationals"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(International,self).save(*args,**kwargs)

class Economic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Economic"
        verbose_name_plural = "Economics"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Economic,self).save(*args,**kwargs)

class Animal_Husbandry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Animal_Husbandry"
        verbose_name_plural = "Animal_Husbandrys"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Animal_Husbandry,self).save(*args,**kwargs)

class Crop_Diseases_and_Protections(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Crop_Diseases_and_Protection"
        verbose_name_plural = "Crop_Diseases_and_Protections"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Crop_Diseases_and_Protections,self).save(*args,**kwargs)

class Technologies_and_Methods(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Technologies_and_Method"
        verbose_name_plural = "Technologies_and_Methods"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Technologies_and_Methods,self).save(*args,**kwargs)

class OtherAgriNews(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "OtherAgriNew"
        verbose_name_plural = "OtherAgriNews"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(OtherAgriNews,self).save(*args,**kwargs)


class Positive_sentiment(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Positive_sentiment"
        verbose_name_plural = "Positive_sentiments"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Positive_sentiment,self).save(*args,**kwargs)

class Negative_sentiment(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Negative_sentiment"
        verbose_name_plural = "Negative_sentiments"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Negative_sentiment,self).save(*args,**kwargs)

class Not_Time_sensitive(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Not_Time_sensitive"
        verbose_name_plural = "Not_Time_sensitives"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Not_Time_sensitive,self).save(*args,**kwargs)

class Time_sensitive(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    text = models.TextField()
    date = models.DateTimeField(null=True,blank=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Time_sensitive"
        verbose_name_plural = "Time_sensitives"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Time_sensitive,self).save(*args,**kwargs)

