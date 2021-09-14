from django.shortcuts import render, redirect
from .models import Employee
from .models import Département
from .formulaire import EmployeeForm
from .formulaire import DepartementForm
from django.contrib import messages


def liste_employees(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'actions/index.html', context)





def ajouter_employees(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('prenom')} a été ajouté avec succés")
        return redirect('liste')

    context = {
        'form': form,
    }
    return render(request, 'actions/ajouter.html', context)


def modifier_employees(request, id=None):
    one_emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=one_emp)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('prenom')} a été modifié")
        return redirect('liste')

    context = {
        'form': form,
    }
    return render(request, 'actions/modifier.html', context)


def one_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    context = {
        'emp': emp
    }
    return render(request, 'actions/voirEmployee.html', context)


def supprimer_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        messages.add_message(request, messages.INFO, f"Employé {emp.prenom} est supprimé")
        return redirect('liste')
    context = {
        'emp': emp
    }
    return render(request, 'actions/supprimer.html', context)


def voirDepartement(request):
    emps = Département.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'actions/voirDepartement.html', context)


def ajoutDepartement(request):
    form = DepartementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('nom')} a été ajouté avec succés")
        return redirect('voirDepartement')

    context = {
        'form': form,
    }
    return render(request, 'actions/ajoutDepartement.html', context)


def modifierDepartement(request, id=None):
    one_emp = Département.objects.get(id=id)
    form = DepartementForm(request.POST or None, request.FILES or None, instance=one_emp)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('nom')} a été modifié")
        return redirect('voirDepartement')

    context = {
        'form': form,
    }
    return render(request, 'actions/modifierDepartement.html', context)

def supprimerDepartement(request, id=None):
    emp = Département.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        messages.add_message(request, messages.INFO, f"Département {emp.nom} est supprimé")
        return redirect('voirDepartement')
    context = {
        'emp': emp
    }
    return render(request, 'actions/supprimerDepartement.html', context)