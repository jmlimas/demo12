from .models import factura, Empresa
from django.views.generic import ListView,TemplateView,CreateView,UpdateView
from .forms import FacturaForm
#from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

 

 
class IndexView(TemplateView):
	template_name = 'core/index.html'
	 

class ListArticulos(ListView):
	context_object_name = 'factura'
	template_name = 'core/movie_list.html'
	model = factura
	paginate_by  = 15
	success_url = '/'
	

class AddNuevo(CreateView):
	form_class = FacturaForm
	model = factura
	template_name = 'core/factura2_form.html'
	success_url  = '/lista'


	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddNuevo,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddNuevo, self).form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(AddNuevo,self).get_context_data(**kwargs)
		context['esmpresa'] = Empresa.objects.all()  
		return context


class UpdateArticulo(UpdateView):
	template_name = 'core/factura2_form.html'
	form_class = FacturaForm
	model = factura
	success_url = reverse_lazy('principal_app:list')
	

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateArticulo, self).form_valid(form)

