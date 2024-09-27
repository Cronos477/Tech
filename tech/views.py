from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os

def index(request):
    print(os.getenv('CLIENT_ID_GITHUB'))
    return render(request, 'index.html')

@login_required
def members(request):
    return render(request, 'members.html')