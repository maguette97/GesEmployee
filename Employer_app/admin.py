from django.contrib import admin
from .models import Département, Employee

# Register your models here.
admin.site.register(Département)
admin.site.register(Employee)


class Département(admin.ModelAdmin):
	pass
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
# Register your models here.
