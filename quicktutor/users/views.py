from django.shortcuts import render
from django.views import generic
from .models import Homepage
from .forms import HomepageForm

# Create your views here.
class HomepageView(generic.CreateView):
    model = Homepage
    #form_class = HomepageForm
    template_name = 'users/homepage.html'
    fields = ['name', 'location', 'subject', 'courseNumber', 'time', 'description']
    #success_url = 'myapp/success.html'
class requestListView(generic.ListView):
    model = Homepage
    template_name = 'users/requestList.html'
