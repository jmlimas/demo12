from django.db import models

from django.conf import settings
 
class TimeStampModel(models.Model):

 	ceated = models.DateTimeField(auto_now_add=True)
 	modified  = models.DateTimeField(auto_now=True)

 	class Meta:
 		abstract = True

class Empresa(TimeStampModel):
	nombre = models.CharField(max_length=300)
	rfc = models.CharField(max_length=30)
	contacto = models.CharField(max_length=150)
	telefono = models.CharField(max_length=30)
	creado = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class factura(TimeStampModel):
	op = (
			('PESO MXN', 'PESO MXN'),
			('DOLAR', 'DOLAR'),
		)
	op2 = (
			('Aprobado', 'Aprobado'),
			('Por pagar', 'Por Pagar'),
			('Pagado', 'Pagado'),
			('Pagado-Complemento','Pagado-Complemento'),
		)

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	numFactura = models.CharField(max_length=20)
	concepto = models.CharField(max_length=250)
	importe = models.DecimalField(max_digits=8, decimal_places=2)
	iva = models.DecimalField(max_digits=8, decimal_places=2)
	total = models.DecimalField(max_digits=8, decimal_places=2)
	moneda = models.CharField(max_length=9, choices=op)
	estatus = models.CharField(max_length=20,choices=op2)
	fechaRecepcion = models.DateField()
	xml = models.ImageField(upload_to='xml/',null=True,blank=True)
	pdf = models.ImageField(upload_to='pdf/',null=True,blank=True)
	otros = models.ImageField(upload_to='otros/',null=True,blank=True)

	def __str__(self):
		return self.numFactura



