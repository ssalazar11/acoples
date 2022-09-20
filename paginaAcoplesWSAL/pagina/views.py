from django.shortcuts import render
from .forms import productoForm
# Create your views here.

def index(request):
    form=productoForm()
    context={'form':form}
    return render(request, 'index.html', context)