from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.forms import UserForm
from accounts.models import User, UserProfile
from accounts.utils import detectUser, send_verification_email
from vendor.forms import VendorForm
from vendor.models import Vendor
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode


# Create your views here.


def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congratulation! Your account is activated.")
        return redirect("myAccount")
    else:
        messages.error(request, "Invalid activation link")
        return redirect("myAccount")


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already registered.")
        return redirect("myAccount")
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
            return redirect("myAccount")
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "accounts/registerUser.html", context)


def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already registered.")
        return redirect("myAccount")
    if request.POST:
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():

            # get user data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # create user and user profile
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.role = User.VENDOR
            user.save()
            user_profile = UserProfile.objects.get(user=user)

            # create vendor
            vendor_name = v_form.cleaned_data["vendor_name"]
            vendor = Vendor(
                user=user,
                user_profile=user_profile,
                vendor_name=vendor_name,
                vendor_license=v_form.cleaned_data["vendor_license"],
                vendor_slug=slugify(vendor_name) + "-" + str(user.id),
            )
            vendor.save()

            # also i can use below code the vendor is passed to the form as instance to save the vendor in database
            # v_form = VendorForm(request.POST, instance=vendor)
            # v_form.save()
    else:
        form = UserForm()
        v_form = VendorForm()
    context = {"form": form, "v_form": v_form}
    return render(request, "accounts/registerVendor.html", context)


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("myAccount")
    if request.POST:
        email = request.POST[
            "email"
        ]  # not using cleaned_data because we are not using form
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("myAccount")

        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    return render(request, "accounts/login.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "You are logged out.")
    return redirect("login")


@login_required(
    login_url="login"
)  # if user is not logged in then redirect to login page
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)


@login_required(
    login_url="login"
)  # if user is not logged in then redirect to login page
@user_passes_test(
    check_role_customer
)  # Decorator for views that checks that the user passes the given test, redirecting to the log-in page if necessary. The test should be a callable that takes the user object and returns True if the user passes.
def custDashboard(request):
    # orders = Order.objects.filter(user=request.user, is_ordered=True)
    # recent_orders = orders[:5]
    # context = {
    #     "orders": orders,
    #     "orders_count": orders.count(),
    #     "recent_orders": recent_orders,
    # }
    return render(request, "accounts/custDashboard.html")


@login_required(
    login_url="login"
)  # if user is not logged in then redirect to login page
@user_passes_test(
    check_role_vendor
)  # Decorator for views that checks that the user passes the given test, redirecting to the log-in page if necessary. The test should be a callable that takes the user object and returns True if the user passes.
def vendorDashboard(request):
    # vendor = Vendor.objects.get(user=request.user)
    # orders = Order.objects.filter(vendors__in=[vendor.id], is_ordered=True).order_by(
    #     "created_at"
    # )
    # recent_orders = orders[:10]

    # # current month's revenue
    # current_month = datetime.datetime.now().month
    # current_month_orders = orders.filter(
    #     vendors__in=[vendor.id], created_at__month=current_month
    # )
    # current_month_revenue = 0
    # for i in current_month_orders:
    #     current_month_revenue += i.get_total_by_vendor()["grand_total"]

    # # total revenue
    # total_revenue = 0
    # for i in orders:
    #     total_revenue += i.get_total_by_vendor()["grand_total"]
    # context = {
    #     "orders": orders,
    #     "orders_count": orders.count(),
    #     "recent_orders": recent_orders,
    #     "total_revenue": total_revenue,
    #     "current_month_revenue": current_month_revenue,
    # }
    return render(request, "accounts/vendorDashboard.html")
