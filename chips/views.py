from django.shortcuts import render
from .models import Chip

def index(request):
    chips = Chip.objects.all()
    return render(request, 'chips/index.html', {'chips': chips})
