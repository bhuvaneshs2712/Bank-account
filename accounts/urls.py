from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('personal-details/', views.personal_details, name='personal_details'),
    path('family-details/<int:personal_id>/', views.family_details, name='family_details'),
    path('nominee-details/<int:personal_id>/', views.nominee_details, name='nominee_details'),
    path('account-details/<int:personal_id>/', views.account_details, name='account_details'),
    path('account-summary/<int:personal_id>/', views.account_summary, name='account_summary'),
    path('account-detail/<int:personal_id>/', views.account_detail_view, name='account_detail_view'),
    path('edit-personal/<int:personal_id>/', views.edit_personal_details, name='edit_personal_details'),
    path('edit-family/<int:personal_id>/', views.edit_family_details, name='edit_family_details'),
    path('edit-nominee/<int:personal_id>/', views.edit_nominee_details, name='edit_nominee_details'),
    path('edit-account/<int:personal_id>/', views.edit_account_details, name='edit_account_details'),
    path('search-accounts/', views.search_accounts, name='search_accounts'),
] 