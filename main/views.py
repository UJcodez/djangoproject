from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def home(request):
	return render(request, 'main/home.html')

def projects(request):
	return render(request, 'main/projects.html')

def contact(request):
	return render(request, 'main/contact.html')

