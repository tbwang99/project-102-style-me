from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

app_name = 'accounts'
urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    # path('', views.index, name='index'),
    
    #Profile
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('request/list', views.requestListView.as_view(), name='requestList'),
]