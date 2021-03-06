
 
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from .views import dashboard_cost, dashboard_energy,  MotorDataListView


app_name = 'dashboard'
urlpatterns = [
    path('',  MotorDataListView.as_view(), name='dashboard_custom'),
    #path('', dashboard_custom, name='dashboard_custom'),
    path('energy', dashboard_energy, name='dashboard_energy'),
    path('cost', dashboard_cost, name='dashboard_cost'),
]

