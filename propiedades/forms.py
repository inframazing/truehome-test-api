from django import forms
from .models import Propiedad


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ('name', 'address', 'square_meters', 'email')
        labels = {
            'name': 'Nombre',
            'address': 'Dirección',
            'square_meters': 'Metros Cudadrados (m²)',
            'email': 'Correo'
        }

    def __init__(self, *args, **kwargs):
        super(PropiedadForm, self).__init__(*args, **kwargs)