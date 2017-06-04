from django.shortcuts import render,redirect
from django.http import Http404
from .forms import ExpenseForm



from cost_management.models import Expense

def my_expense(request):
	expenses=Expense.objects.all()
	context={'expenses':expenses}
	return render(request,'cost/expense.html',context)

def add_expense(request):
	if request.method =='POST':
		form= ExpenseForm(request.POST)
		form.save()
		return redirect('cost-list')
	else:
		form=ExpenseForm
	return render(request,'cost/add_expense.html',{
			'form':form
		})
