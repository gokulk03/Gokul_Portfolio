from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'signup.html')

def handleLogin(request):
    return render(request,'handleLogin.html')

def handleLogout(request):
    return render(request,'handleLogout.html')


