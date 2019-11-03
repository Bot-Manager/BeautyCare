from django.shortcuts import render
from .models import Reservas
from .forms import ReservarServicioForm
from reservas.models import Reservas

# Create your views here.

def reserva_servicio(request):
    
    context = {}

    return render(request , 'Reservas/reservas.html' , context)