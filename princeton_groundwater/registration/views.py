from django.shortcuts import render, get_list_or_404
from .models import Course

def index(request):
  context = { 'courses': get_list_or_404(Course) } # use GLO404 to handle empty query sets
  return render(request, 'registration/index.html', context)