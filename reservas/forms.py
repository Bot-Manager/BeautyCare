from django import forms
from .models import Reservas


class ReservarServicioForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'