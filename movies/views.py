from django.shortcuts import render

# Create your views here.

# first page
def index(request):
	return render(request, 'movies/index.html')