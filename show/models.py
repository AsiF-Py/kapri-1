from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class RJProfile(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    picture = models.ImageField(upload_to='RJ Profile')
    biography = models.TextField()

    facebook_profile = models.CharField(blank=True,null=True,max_length=200)
    insta_profile = models.CharField(blank=True,null=True,max_length=200)
    linkedin_profile = models.CharField(blank=True,null=True,max_length=200)
    x_profile = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.name


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    host = models.ForeignKey(RJProfile,on_delete=models.CASCADE,related_name='host')
    gest = models.ManyToManyField(RJProfile)
    image = models.ImageField(upload_to='show',default=None,blank=True,null=True)
    sound = models.FileField(upload_to='sound',default=None,blank=True,null=True)

    def __str__(self):
        return f'{self.title} By {self.host}'

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def duration(self):
        start_datetime = datetime.combine(datetime.today(), self.start_time)
        end_datetime = datetime.combine(datetime.today(), self.end_time)
        duration_timedelta = end_datetime - start_datetime

        # Convert duration to minutes
        duration_minutes = duration_timedelta.total_seconds() // 60
        return int(duration_minutes)