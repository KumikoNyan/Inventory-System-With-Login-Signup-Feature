from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_supplier/<int:pk>/', views.view_supplier, name='view_supplier'),
    path('', views.SignIn, name='SignIn'),
    path('view_bottles/<int:pk>/', views.view_bottles, name='view_bottles'),
    path('add_bottle/<int:pk>/', views.add_bottle, name='add_bottle'),
    path('Register', views.Register, name='Register'),
    path('SignIn_Error', views.SignIn_Error, name ="SignIn_Error"),
    path('Register_Error', views.Register_Error, name ="Register_Error"),
    path('ManageAcc/<int:pk>/', views.ManageAcc, name='ManageAcc'),
    path('DeleteAcc/<int:pk>/', views.DeleteAcc, name='DeleteAcc'),
    path('NewPass/<int:pk>/', views.NewPass, name='NewPass'),
    path('ChangePass/<int:pk>/', views.ChangePass, name='ChangePass'),
    path('view_bottle_details/<int:pk>/<int:pk1>/', views.view_bottle_details, name='view_bottle_details'),
    path('delete_bottle/<int:pk>/<int:pk1>/', views.delete_bottle, name='delete_bottle'),
    path('SignOut', views.SignOut, name='SignOut'),
]