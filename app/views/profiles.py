from django.shortcuts import redirect, render
from app.common.budget import calculate_budget_left
from app.common.profile import get_profile
from app.forms.profile import ProfileForm, DeleteProfileForm
from app.models import Expenses


def profile_index(req):
    profile = get_profile()
    expenses = Expenses.objects.all()
    profile.budget_left = calculate_budget_left(profile, expenses)
    context = {
        'profile': profile,
    }
    return render(req, 'profile.html', context)


def create_profile(req):
    if req.method == 'GET':
        context = {
            'form': ProfileForm(),
        }
        return render(req, 'home-no-profile.html', context)
    else:
        form = ProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(req, 'home-no-profile.html', context)


def edit_profile(req):
    profile = get_profile()
    if req.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(req, 'profile-edit.html', context)
    else:
        form = ProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile index')
        else:
            context = {
                'form': form,
            }
            return render(req, 'profile-edit.html', context)


def delete_profile(req):
    profile = get_profile()
    if req.method == 'GET':
        context = {
            'form': DeleteProfileForm(instance=profile),
        }
        return render(req, 'profile-delete.html', context)
    else:
        profile.delete()
        Expenses.objects.all().delete()
        return redirect('index')
