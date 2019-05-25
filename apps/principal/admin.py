from django.contrib import admin

from .models import  Empresa,factura

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','rfc')
	list_filter = ('nombre',)

class facturaAdmin(admin.ModelAdmin):
	list_display = ('id','empresa','numFactura','concepto')
	list_filter = ('empresa',)


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(factura,facturaAdmin)

