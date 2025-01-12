from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
# Create your views here.
def home(request):
    return render(request,'home.html')

class Tasklist(ListView):
    model = Task
    context_object_name = 'tasks' #spesifye non model la nan template la
    
