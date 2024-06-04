from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('contacts/', views.contacts, name='contacts_page'),
    path('about/', views.about, name='about_page'),
    path('home/', views.home, name='home_page'),
]



