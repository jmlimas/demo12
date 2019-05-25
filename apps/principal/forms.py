from django import forms
from .models import factura

class FacturaForm(forms.ModelForm):
	class Meta:
		model = factura
		exclude = ['user']

	numFactura = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Numero Factura','size': '20'}))
	concepto = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Concepto de compra','size': '60'}))
       