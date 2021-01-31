# jobs/models.py

from django.db import models
from django.template.defaultfilters import slugify
from config import settings


# MODEL: Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(default=None,editable=False)


    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args,**kwargs)



# MODEL: Job
class Job(models.Model):
    title 	= models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    CHOICES = (
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('freelance','Freelance'),
        ('internship','Internship'),
        ('temporary','Temporary'),
    )

    job_type 	= models.CharField(max_length=20,blank=False,default=None,choices=CHOICES)
    location 	= models.CharField(max_length=200,blank=False,default=None)
    description = models.TextField(blank=False,default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug 		= models.SlugField(default=None,editable=False)
    employer 	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    category    = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="jobs", default=None)

    def __str__(self):
        return self.title


    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)


    class Meta:
        ordering = ('-id',)