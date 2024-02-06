from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserForm
from accounts.models import User

# Create your views here.


def registerUser(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]

            # user = form.save(commit=False)
            # user.role = User.CUSTOMER
            # user.save()
            # alternative below
            user = User(role=User.CUSTOMER)
            user.set_password(password)
            form = UserForm(request.POST, instance=user)
            form.save()
            messages.success(request, "User Created Successfully")
            return redirect("registerUser")
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "accounts/registerUser.html", context)
