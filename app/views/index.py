from django.shortcuts import render

from app.common.budget import calculate_budget_left
from app.models import Profile, Expenses
from app.views.profiles import create_profile


def index(req):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expenses.objects.all()

        profile.budget_left = calculate_budget_left(profile, expenses)

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(req, 'home-with-profile.html', context)
    else:
        return create_profile(req)
