from django.shortcuts import render
from .forms import ImageForm, LoginForm, RegisterForm
from .models import Image, LoginModel, RegisterModel
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'home.html', {'img':img, 'form':form})

def set_session(request):
    request.session['username'] = 'john_doe'
    request.session['email'] = 'john@example.com'
    return render(request, 'set_session.html')

def get_session(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'guest@example.com')
    return render(request, 'get_session.html', {'username': username, 'email': email})

def delete_session(request):
    request.session.flush()
    return render(request, 'delete_session.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

def register(request):
    error_message = None  # Initialize error message as None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Checking for username
            if RegisterModel.objects.filter(username=username).exists():
                error_message = "Username already taken. Please choose a different one."
            else:
                r = RegisterModel.objects.create(username=username, email=email, password=password)
                r.save()
                return render(request, 'registration.html', {'form': form, 'username': username, 'email': email})
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form, 'error_message': error_message})