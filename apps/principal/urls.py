
from django.urls import path

from . import views
app_name = 'principal'

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('lista/',views.ListArticulos.as_view()),
    path('nuevo/',views.AddNuevo.as_view()),
]



