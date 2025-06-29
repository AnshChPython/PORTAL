from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        date = datetime.now()
        
        
    return render(request,'account/index.html')

def login(request):
    return render(request,'account/login.html')    