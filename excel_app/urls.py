from django.urls import path
from . import views

urlpatterns = [
    path('get-excel-data/', views.get_excel_data, name='get_excel_data'),
    path('', views.display_excel_data, name='display_excel_data'),
]
 