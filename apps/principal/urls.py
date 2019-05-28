
from django.urls import path
from . import views
app_name = 'principal'

urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('lista/',views.ListArticulos.as_view(),name='list'),
    path('nuevo/',views.AddNuevo.as_view()),
    path('update/<int:pk>/',views.UpdateArticulo.as_view(),name = 'update_articulo'),
    
]
 