from django import forms


class NahualBuscarForm(forms.Form):
    fecha = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
