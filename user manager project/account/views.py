from django.shortcuts import render ,redirect
from . forms import RegisterForm
from . models import CustomeUser
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request , 'home.html' )


def home(request):
    return render(request,'home.html')
def register_view(request):

    #print(request.method,'mmmm')
    #print(request.POST,'dataaaa')

    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method=='POST':
        form=RegisterForm(request.POST)
        #print(form)
        if form.is_valid():

            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            user=CustomeUser(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            #hash password
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email =request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            request ,
            email=email,
            password=password
        )
        print(user, 'uuuuuuuuuuuuuuuuuuu')
        if user is not None:
            login(request , user)
            return redirect('home')

    return render(request, 'login.html')

def logout_view(request):
    print('before logout')
    print(request.user)
    print(request.user.is_authenticated)

    logout(request)

    print('after logout')
    print(request.user)
    print(request.user.is_authenticated)
    

    return redirect('login')