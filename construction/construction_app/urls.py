from django.urls import path
from . import views
 
urlpatterns = [
    path('project/', views.ProjectView.as_view()),
    path('labours/', views.LabourView.as_view()),
    path('labours/<int:pk>/', views.LabourView.as_view()),
    path('equipments/', views.EquipmentView.as_view()),
    path('equipments/<int:pk>/', views.EquipmentView.as_view()),
    path('materials/<int:pk>/', views.MaterialView.as_view()),
    path('materials/', views.MaterialView.as_view()),
    path('project/<int:pk>/',views.ProjectView.as_view()),

]