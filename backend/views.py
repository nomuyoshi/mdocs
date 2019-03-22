from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {})

def terms(request):
    return render(request, 'terms.html', {})

@login_required
def index(request):
    return render(request, 'application.html', {})
