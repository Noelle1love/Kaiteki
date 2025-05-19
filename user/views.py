from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")# куда перенаправить после регистрации
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form})
