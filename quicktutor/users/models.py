#import datetime

from django.db import models
#from django.utils import timezone
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
SUBJECT_CHOICES = (
    ('Subject','SUBJECT'),
    ('APMA', 'MATH'),
    ('CS', 'COMPUTER SCIENCE'),
    ('GCOM', 'BUSINESS'),
    ('BIOL', 'BIOLOGY'),
    ('CHEM', 'CHEMISTRY'),
)
TIME_INTERVALS = (
    ('5','5'),
    ('15','15'),
    ('30','35'),
    ('60','60'),
    ('75','75'),
    ('90','90'),
    ('120','120'),
)

class Homepage(models.Model):
    name = models.CharField(max_length=50,default='------')
    location = models.CharField(max_length=50, default='------')
    subject = models.CharField(max_length=17, choices=SUBJECT_CHOICES, default='Subject')
    course = models.CharField(max_length=50, default='------')
    number = models.CharField(max_length=50, default='------')
    length = models.CharField(max_length=17, choices=TIME_INTERVALS, default='5')
    description = models.TextField(max_length=300, default='------')

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('users:homepage')
