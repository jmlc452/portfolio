from django import forms

class contacto_form(forms.Form):
    nombre = forms.CharField(label="nombre",required=True)
    email = forms.CharField(label="email",  required=True)
    contenido = forms.CharField(widget=forms.Textarea,label="contenido")

    