from django.urls import path
from . import views
from .views import diabetes,BreastCancer
urlpatterns = [
    path('', views.home, name='Blog-Home'),
    path('about/', views.about, name='Blog-about'),
    path('diabetes/',diabetes.as_view(),name='diabetes-data'),
    path('BreastCancer/',BreastCancer.as_view(), name='BreastCancer-data')
]