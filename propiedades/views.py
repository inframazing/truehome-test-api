from django.shortcuts import render, redirect
from .forms import PropiedadForm
from .models import Propiedad


def propiedad_list(request):
    context = {'propiedad_list': Propiedad.objects.all()}
    return render(request, "propiedades/propiedad_list.html", context)


def propiedad_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PropiedadForm()
        else:
            propiedad = Propiedad.objects.get(pk=id)
            form = PropiedadForm(instance=propiedad)
        return render(request, "propiedades/propiedad_form.html", {'form': form})
    else:
        if id == 0:
            form = PropiedadForm(request.POST)
        else:
            propiedad = Propiedad.objects.get(pk=id)
            form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
        return redirect('/propiedades/list')


def propiedad_delete(request, id):
    propiedad = Propiedad.objects.get(pk=id)
    propiedad.delete()
    return redirect('/propiedades/list')
