from django.shortcuts import render

from accounts.forms import UserForm

# Create your views here.

def registerUser(request):
    form = UserForm()
    context= {'form': form}
    return render(request, 'accounts/registerUser.html', context)