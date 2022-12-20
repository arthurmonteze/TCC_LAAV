from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import DispForm
from .forms import ProfForm
from django.contrib import messages

from .models import Dispositivo
from .models import Professor
from .models import Secretaria
from .models import Usuario
from .models import Emprestimo

#PARTE PRINCIPAL
@login_required
def infoDisp(request):
    disp_list = Dispositivo.objects.all().order_by('-created_at')

    paginator = Paginator(disp_list, 8)

    page = request.GET.get('page')

    disp = paginator.get_page(page)

    context = {'disp':disp,}
    return render(request, 'tcc/info.html', context)

@login_required
def agend(request):
    return render(request, 'tcc/agend.html')

@login_required
def prof(request):
    prof_list = Professor.objects.all()

    paginator = Paginator(prof_list, 8)

    page = request.GET.get('page')

    prof = paginator.get_page(page)

    return render(request, 'tcc/prof.html', {'prof': prof})

#DISPOSITIVOS
@login_required
def projView(request, id):
    proj = get_object_or_404(Dispositivo, pk=id)
    return render(request, 'tcc/proj.html', {'proj': proj})

@login_required
def newDisp(request):
    if request.method == 'POST':
        form = DispForm(request.POST)

        if form.is_valid():
            disp = form.save(commit=False)
            disp.save()
            return redirect('/info')
    else:
        form = DispForm()
        return render(request, 'tcc/adddisp.html', {'form': form})
@login_required
def editDisp(request, id):
    disp = get_object_or_404(Dispositivo, pk=id)
    form = DispForm(instance=disp)

    if(request.method == 'POST'):
        form = DispForm(request.POST, instance=disp)

        if(form.is_valid()):
            disp.save()
            return redirect('/info')
        else:
            return render(request, 'tcc/editdisp.html', {'form': form, 'disp': disp})

    else:
        return render(request, 'tcc/editdisp.html', {'form': form, 'disp': disp})
@login_required
def deleteDisp(request, id):
    disp = get_object_or_404(Dispositivo, pk=id)
    disp.delete()

    messages.info(request, 'Dispositivo deletado com sucesso.')

    return redirect('/info')

#PROFESSORES
@login_required
def profView(request, id):
    prof = get_object_or_404(Professor, pk=id)
    return render(request, 'tcc/infoprof.html', {'prof': prof})

@login_required
def newProf(request):
    if request.method == 'POST':
        form = ProfForm(request.POST)

        if form.is_valid():
            prof = form.save(commit=False)
            prof.save()
            return redirect('/prof')
    else:
        form = ProfForm()
        return render(request, 'tcc/addprof.html', {'form': form})

@login_required
def editProf(request, id):
    prof = get_object_or_404(Professor, pk=id)
    form = ProfForm(instance=prof)

    if(request.method == 'POST'):
        form = ProfForm(request.POST, instance=prof)

        if(form.is_valid()):
            prof.save()
            return redirect('/prof')
        else:
            return render(request, 'tcc/editprof.html', {'form': form, 'prof': prof})

    else:
        return render(request, 'tcc/editprof.html', {'form': form, 'prof': prof})
@login_required
def deleteProf(request, id):
    prof = get_object_or_404(Professor, pk=id)
    prof.delete()

    messages.info(request, 'Professor deletado com sucesso.')

    return redirect('/prof')