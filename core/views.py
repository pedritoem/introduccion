#vista completa y tengo control de mis vistas, clases y funciones
from django.views.generic import View 
from django.shortcuts import render

#Vista de clases llamada view, Nos da acceso a ambos getRequest y postRequest
class HomeView(View):
    def get(self,request,*args,**kwargs ):   # para poder llamar; mostrar info. self se usa cuando se trabaja una clase
        context={
            
        }
        return render(request, 'index.html', context)                                # *args,**kwargs hace referencia a cualquier param que el obj del request pueda tner







