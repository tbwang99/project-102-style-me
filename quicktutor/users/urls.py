from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

app_name = 'users'
urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    # path('', views.index, name='index'),
    
    #Login, Logout, Registration
    # url(r'^login/$', LoginView.as_view(), {'template_name': 'users/login.html'}, name='login'),
    # url(r'^logout/$', LogoutView.as_view(), {'template_name': 'users/logout.html'}, name='logout'),
    # url(r'^register/$', views.register, name='register'),
    
    #Profile
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    # url(r'^profile/$', views.view_profile, name='view_profile'),
    # url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    #Password
    # url(r'^profile/password/$', views.change_password, name='change_password'),
    # url(r'^reset-password/$', PasswordResetView.as_view(), {'template_name': 'users/reset_password.html', 'post_reset_redirect': 'users/password_reset_done', 'email_template_name': 'users/reset_password_email.html'}, name='reset_password'),
    # url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), {'template_name': 'users/reset_password_done.html'}, name='password_reset_done'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), {'template_name': 'users/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
    # url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(),{'template_name': 'users/reset_password_complete.html'}, name='password_reset_complete')

]