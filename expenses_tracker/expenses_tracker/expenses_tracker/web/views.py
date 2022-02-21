import os

from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker.web.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from expenses_tracker.web.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    if not profile:
        return redirect('create profile')

    context = {
        'expenses': expenses,
        'budget_left': budget_left,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('home page')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    return render(request, 'profile.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
