from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_list, name='crud_list'),
    path('crud/<int:pk>/', views.crud_detail, name='crud_detail'),
    path('crud/new/', views.crud_create, name='crud_create'),
    path('crud/<int:pk>/edit/', views.crud_update, name='crud_update'),
    path('crud/<int:pk>/delete/', views.crud_delete, name='crud_delete'),
    path('hosp/<int:pk>/', views.hosp_detail, name='hosp_detail'),
    path('hosp/new/', views.hosp_create, name='hosp_create'),
    path('hosp/<int:pk>/edit/', views.hosp_update, name='hosp_update'),
    path('hosp/<int:pk>/delete/', views.hosp_delete, name='hosp_delete'),
    path('admission/', views.admis_list, name='admis_list'),
    path('admission/<int:pk>/', views.admis_detail, name='admis_detail'),
    path('admission/new/', views.admis_create, name='admis_create'),
    path('admission/<int:pk>/edit/', views.admis_update, name='admis_update'),
    path('admission/<int:pk>/delete/', views.admis_delete, name='admis_delete'),
    # path('get_crud_details/', views.get_crud_details, name='get_crud_details'),
    path('get_crud_form/', views.get_crud_form, name='get_crud_form'),
    path('admissions/<str:phealth_no>/', views.admission_list, name='admission_list'),
]