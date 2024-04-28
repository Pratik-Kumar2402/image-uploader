from django.shortcuts import render, redirect
from .forms import ImageForm, LoginForm, RegisterForm
from .models import Image, RegisterModel

def home(request):
    if "logged_in" not in request.session:
        return redirect("register")

    username = request.session.get("logged_in")
    if request.method == "POST":
        form_data = request.POST.copy()
        form_data["username"] = username
        form = ImageForm(form_data, request.FILES)
        if form.is_valid():
            # print(form_data['username'])
            form.save()
    else:
        form = ImageForm()

    img = Image.objects.all()
    return render(
        request, "home.html", {"img": img, "form": form, "username": username}
    )


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = RegisterModel.objects.get(username=username)
                if user.password == password:
                    request.session["logged_in"] = username
                    return redirect("home")
                else:
                    return render(
                        request,
                        "login.html",
                        {"form": form, "error_message": "Incorrect password"},
                    )
            except RegisterModel.DoesNotExist:
                return render(
                    request,
                    "login.html",
                    {"form": form, "error_message": "Make sure you are registered"},
                )
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if "logged_in" in request.session:
        request.session.flush()

    error_message = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Checking for username
            if RegisterModel.objects.filter(username=username).exists():
                error_message = "Username already taken. Please choose a different one."
            else:
                r = RegisterModel.objects.create(
                    username=username, email=email, password=password
                )
                r.save()
                return render(
                    request,
                    "registration.html",
                    {"form": form, "username": username, "email": email},
                )
    else:
        form = RegisterForm()
    return render(
        request, "registration.html", {"form": form, "error_message": error_message}
    )

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')