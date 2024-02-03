from django.shortcuts import render
def home(Request):
    return render(Request, 'home.html')