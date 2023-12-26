from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        print(get_email)
        print(get_password)
        print(get_confirm_password)
    return render(request,'signup.html')

def handleLogin(request):
    return render(request,'login.html')

def handleLogout(request):
    return render(request,'logout.html')


