from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero

# Create your views here.
def index(request):
  return render(request, 'superheroes/index.html')

def view(request):
  all_superheroes = Superhero.objects.all()
  context = {
    'all_superheroes': all_superheroes
  }
  return render(request, 'superheroes/view.html', context)

def detail(request, superhero_id):
  try:
    superhero = Superhero.objects.get(pk=superhero_id)
  except Superhero.DoesNotExist:
    raise Http404("Superhero does not exist")
  return render(request, 'superheroes/detail.html')