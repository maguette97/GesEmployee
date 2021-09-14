from django.forms import ModelForm
from .models import Employee
from .models import Département

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['prenom', 'nom', 'mail', 'tel', 'date_embauche']

class DepartementForm(ModelForm):
	class Meta:
		model = Département
		fields = ['nom']
		