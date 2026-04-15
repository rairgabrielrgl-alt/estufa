from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/monitoramento/painel/')

urlpatterns = [
    path('', home),  # 👈 ADICIONA ISSO
    path('admin/', admin.site.urls),
    path('monitoramento/', include('monitoramento.urls')),
]