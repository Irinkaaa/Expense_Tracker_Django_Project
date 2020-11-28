from django.shortcuts import render, redirect

from app.forms.expense import ExpenseForm, DeleteExpenseForm
from app.models import Expenses


def create_expense(req):
    if req.method == 'GET':
        context = {
            'form': ExpenseForm(),
        }
        return render(req, 'expense-create.html', context)
    else:
        form = ExpenseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(req, 'expense-create.html', context)


def edit_expense(req, pk):
    expense = Expenses.objects.get(pk=pk)
    if req.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }
        return render(req, 'expense-edit.html', context)
    else:
        form = ExpenseForm(req.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'expense': expense,
                'form': form,
            }
            return render(req, 'expense-edit.html', context)


def delete_expense(req, pk):
    expense = Expenses.objects.get(pk=pk)
    if req.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpenseForm(instance=expense),
        }
        return render(req, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('index')
