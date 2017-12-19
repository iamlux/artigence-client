from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index_new.html', locals())

def list(request):
	return render(request, 'grid_new.html', locals())

def task(request):
	return render(request, 'task-detail.html', locals())