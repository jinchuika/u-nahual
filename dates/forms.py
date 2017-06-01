from django import forms


class NahualBuscarForm(forms.Form):
    day = forms.CharField(
        label="Día",
        widget=forms.NumberInput(attrs={'class': 'form-control transparent-input', 'min': 1, 'max': 31}))
    month = forms.CharField(
        label="Mes",
        widget=forms.NumberInput(attrs={'class': 'form-control transparent-input', 'min': 1, 'max': 12}))
    year = forms.CharField(
        label="Año",
        widget=forms.NumberInput(attrs={'class': 'form-control transparent-input', 'min': 1900}))
