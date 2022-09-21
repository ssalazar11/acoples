from django.shortcuts import render
from .forms import productoForm
from .models import producto
# Create your views here.

def index(request):
    form=productoForm(request.POST)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request, 'index.html', context)

 def resultado(request, codigo):
    objeto=producto.objects.get(codigo=codigo)
    return render(request)
