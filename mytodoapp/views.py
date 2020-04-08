from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import Todoform
from django.contrib import messages
from .models import Todomodel

# Create your views here.
def addtask(request):
	if request.method=="POST":
		form=Todoform(request.POST)
		obj=Todomodel()
		obj.taskname=request.POST.get('taskname')
		obj.targetdate=request.POST.get('targetdate')
		obj.taskdescp=request.POST.get('taskdescp')
		obj.save()
		return redirect('/./')
	else:
		form=Todoform()
		return render(request,'mytodoapp/taskpage.html',{'form':form})	

def remove(request,pk): 
	item = Todomodel.objects.get(id=pk) 
	if request.method=='POST':
		item.delete()
		return redirect('/././')
	return render(request,'mytodoapp/delete.html',{'item':item}) 

def home(request):
	tasklist=Todomodel.objects.all()
	return render(request,'mytodoapp/home.html',{'tasklist':tasklist})		