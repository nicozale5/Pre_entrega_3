from django import forms


class CargarLiga(forms.Form):
    liga = forms.CharField(required=True, max_length=64)
    pais = forms.CharField(required=True, max_length=64)