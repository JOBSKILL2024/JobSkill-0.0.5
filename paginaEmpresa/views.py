from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PuestoForm
from .models import Puesto
from jobskill1.models import Empresa

# Create your views here.
@login_required
def home(request):
    puestos=Puesto.objects.all()
    return render(request, "paginaEmpresa/editar.html", {"puestos":puestos})
@login_required
def agregar(request):
    if request.method=="POST":
        form=PuestoForm(request.POST)
        if form.is_valid:
            puesto=form.save(commit=False)
            try:
                empresa=Empresa.objects.get(user=request.user)
                puesto.empresa=empresa
                puesto.save()
                return redirect("homeE")
            except Empresa.DoesNotExist:
                form.add_error(None, "No se encontró una empresa asociada con este usuario.")
        else:
            return render(request, "paginaEmpresa/agregar.html", {"form":form})
    else:
        form=PuestoForm()
    return render(request, "paginaEmpresa/agregar.html", {"form":form})
@login_required
def perfil(request):
    return render(request, "paginaEmpresa/perfil.html")
@login_required
def solicitud(request):
    return render(request, "paginaEmpresa/solicitud.html")