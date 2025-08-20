# flights/forms.py
from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        fields =['name','type','price']
        model=Flight
        widgets = {
            'type': forms.Select(choices=Flight.TYPE_CHOICES),
        }
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'price': 'Precio',
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0')
        return price
