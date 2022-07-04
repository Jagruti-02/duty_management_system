from django.http import HttpResponse
from django.shortcuts import render, redirect
from matplotlib.style import context
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


# Create your views here.


def employee_list(request):
    context = {'adminprofile': Employee.objects.all()}
    return render(request, "admin_profile.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/success')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/register/list')


def home(request):
    return render(request, 'home/login.html')


def signin(request):

    if request.method == 'POST':
        login_data = Employee.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        # print("myoutput", username+password)
        # check if user is already registered
        isLoginTrue = 0
        user_data = 0
        for i in login_data:
            if (i.username == username) and (i.password == password):
                isLoginTrue = 1
                user_data = i  # user_data is the user object

        if (isLoginTrue == 1) and (user_data.user_type_id == 1):
            return render(request, "profile.html", {'ldata': login_data})
        elif (isLoginTrue == 1) and (user_data.user_type_id == 2):
            return render(request, "admin_profile.html", {'ldata': login_data})
        else:
            # show error message on same html page
            return render(request, "home/login.html", {'error': 'Invalid username or password'})


def profile(request):
    return render(request, 'profile.html')


def admin_profile(request):
    return render(request, 'admin_profile.html')


def success(request):
    return render(request, 'success.html')


def signout(request):
    logout(request)
    return redirect('/')
