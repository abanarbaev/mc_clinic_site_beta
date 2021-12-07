from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('travma/', views.travma, name='travma'),
    path('gynecology/', views.gynecology, name='gynecology'),

    path('urology/', views.urology, name='urology'),
    path('vaccine/', views.vaccine, name='vaccine'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('firstaid/', views.firstaid, name='firstaid'),
    path('online/', views.online, name='online'),
    path('callhome/', views.callhome, name='callhome'),
    path('vacancies/', views.vacancies, name='vacancies'),

    path('about/', views.about, name='about'),
    path('occasions/', views.occasions, name='occasions'),
    path('articles/', views.articles, name='articles'),

    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    
]
