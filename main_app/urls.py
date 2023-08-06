from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rings/', views.rings_index, name='index'),
    path('rings/<int:ring_id>/', views.rings_detail, name='detail'),
    path('rings/create/', views.RingCreate.as_view(), name='rings_create'),
    path('rings/<int:pk>/update/', views.RingUpdate.as_view(), name='rings_update'),
    path('rings/<int:pk>/delete/', views.RingDelete.as_view(), name='rings_delete'),
    path('rings/<int:ring_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('rings/<int:ring_id>/assoc_owner/<int:owner_id>/', views.assoc_owner, name='assoc_owner'),
    path('rings/<int:ring_id>/remove_owner/<int:owner_id>/', views.remove_owner, name='remove_owner'),
    path('owners/', views.OwnerList.as_view(), name='owners_index'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name='owners_detail'),
    path('owners/create/', views.OwnerCreate.as_view(), name='owners_create'),
    path('owners/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owners_update'),
    path('owners/<int:pk>/delete/', views.OwnerDelete.as_view(), name='owners_delete'),
]