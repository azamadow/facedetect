from django.urls import path

from .import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('hasaba_almak_sanow/', views.hasaba_almak_sanow, name="hasaba_almak_sanow"),
    path('gatnasyk/', views.gatnasyk, name="gatnasyk"),
    path('gatnasyk/<int:category_id>/', get_category, name='category'),
    path('detect/add-detect/', add_detect, name='add_detect'),
    path('delete-detect/<str:pk>/', views.deleteDetect, name='delete-detect'),
    path('detect_form/<str:pk>/', UpdateDetect.as_view(), name='detect_form'),
    path('search/', search, name='search'),
    path('search/<int:category_id>/', get_search_category, name='search_category'),
    path('export_excel_file/', export_excel_file, name='export_excel_file'),
    path('logout/', logout, name='logout'),
]
