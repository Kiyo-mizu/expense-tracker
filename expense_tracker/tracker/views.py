from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForm
# Create your views here.


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request,'expense_list.html',{'expenses':expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request,'add_expense.html',{'form':form})

def delete_expense(request,id):
    expenses = get_object_or_404(Expense,id=id)
    if request.method == 'POST':
        expenses.delete()
        return redirect('expense_list')
    return render(request,'delete_expense.html',{'expenses':expenses})

def update_expense(request,id):
    expenses = get_object_or_404(Expense,id=id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        expenses.amount = amount
        expenses.description = description
        expenses.save()

        return redirect('expense_list')
    return render(request,'update_expense.html',{'expenses':expenses})
    
