from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # request.POST['name']
        if request.POST['password1'] == request.POST['password2']:
            
            # 동일id / 다른 password인 경우 로그인 못하도록~
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
            # ~여기까지

                user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')

        # 동일 id / 다른 password 통과 못하도록~
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
    # ~여기까지
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # DB에 있다면
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # DB에 없다면
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')