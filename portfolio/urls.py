from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('biodata/', views.biodata, name='biodata'),
    path('page2/', views.page2, name='page2')
]