from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserForm
from accounts.models import User, UserProfile
from vendor.forms import VendorForm
from vendor.models import Vendor
from django.utils.text import slugify

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

def registerVendor(request):
    if request.POST:
                form = UserForm(request.POST)
                v_form = VendorForm(request.POST, request.FILES)
                if form.is_valid() and v_form.is_valid():

                    #get user data
                    first_name = form.cleaned_data["first_name"]
                    last_name = form.cleaned_data["last_name"]
                    email = form.cleaned_data["email"]
                    username = form.cleaned_data["username"]
                    password = form.cleaned_data["password"]

                    #create user and user profile
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,password=password)
                    user.role = User.VENDOR
                    user.save()
                    user_profile = UserProfile.objects.get(user=user)
                    
                    #create vendor
                    vendor_name = v_form.cleaned_data['vendor_name']
                    vendor=Vendor(user=user, user_profile=user_profile, vendor_name=vendor_name, vendor_license=v_form.cleaned_data["vendor_license"],vendor_slug = slugify(vendor_name)+'-'+str(user.id))
                    vendor.save()


                    #also i can use below code the vendor is passed to the form as instance to save the vendor in database
                    # v_form = VendorForm(request.POST, instance=vendor)
                    # v_form.save()
    else:
        form = UserForm()
        v_form = VendorForm()
    context={
        "form": form,
        "v_form": v_form
    }
    return render(request, "accounts/registerVendor.html",context)
