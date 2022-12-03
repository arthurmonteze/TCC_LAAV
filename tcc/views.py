from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Dispositivo
from .models import Professor
from .models import Secretaria
from .models import Usuario
from .models import Emprestimo

@login_required
def infoDisp(request):
    disp = Dispositivo.objects.all()
    context = {'disp':disp,}
    return render(request, 'tcc/info.html', context)

@login_required
def agend(request):
    return render(request, 'tcc/agend.html')

def projView(request, id):
    proj = get_object_or_404(Dispositivo, pk=id)
    return render(request, 'tcc/proj.html', {'proj': proj})