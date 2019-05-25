from .models import factura, Empresa
from django.views.generic import ListView,TemplateView,CreateView
from .forms import FacturaForm
 

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

