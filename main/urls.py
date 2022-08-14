from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<str:pk>/', views.detailportfolio, name='detailportfolio'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:pk>/', views.blogdetail, name="blogdetail"),
    path('contact/', views.contact, name='contact'),
    
]
