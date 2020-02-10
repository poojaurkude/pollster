from django.urls import path
from . import views
from django.contrib.auth.models import User
app_name = 'app'
# from django.contrib import admin
# from django.urls import path

urlpatterns = [
    
    path('', views.home,name='home'),
    path('index',views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("register",views.register, name='register'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("voter",views.voter, name='voter')
]