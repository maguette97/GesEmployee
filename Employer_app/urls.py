from django.urls import path
from . import views
urlpatterns = [
    path('', views.liste_employees,name='liste'),
    path('ajouterEmployee/', views.ajouter_employees,name='ajouter'),
    path('modifierEmployee/<int:id>', views.modifier_employees,name='modifier'),
    path('voirEmployee/<int:id>', views.one_employee,name='oneEmp'),
    path('supprimerEmployee/<int:id>', views.supprimer_employee,name='supprimer'),
    path('voirDepartement', views.voirDepartement,name='voirDepartement'),
    path('ajoutDepartement/', views.ajoutDepartement,name='ajoutDepartement'),
    path('modifierDepartement/<int:id>', views.modifierDepartement,name='modifierDepartement'),
     path('supprimerDepartement/<int:id>', views.supprimerDepartement,name='supprimerDepartement'),
]

