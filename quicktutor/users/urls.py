from django.urls import path

from . import views
app_name = 'users'
urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    # path('', views.index, name='index'),
    path('request/list', views.requestListView.as_view(), name='requestList'),
]