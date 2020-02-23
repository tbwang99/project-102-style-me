#import datetime

from django.db import models
#from django.utils import timezone
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
SUBJECT_CHOICES = (
    ('Subject','SUBJECT'),
    ('APMA', 'Math'),
    ('CS', 'Computer Science'),
    ('COMM', 'Business'),
    ('BIOL', 'Biology'),
    ('CHEM', 'Chemistry'),
)
TIME_INTERVALS = (
    ('5','5 minutes'),
    ('15','15 minutes'),
    ('30','35 minutes'),
    ('60','1 hour'),
    ('75','1 hour 15 minutes'),
    ('90','1.5 hour'),
    ('120','2 hours'),
)

class Homepage(models.Model):
    name = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=17, choices=SUBJECT_CHOICES, default='Subject')
    courseNumber = models.CharField(max_length=50, default='')
    time = models.CharField(max_length=17, choices=TIME_INTERVALS, default='5')
    description = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('users:homepage')
