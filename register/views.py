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
    context = {'employee_list': Employee.objects.all()}
    return render(request, "register/employee_list.html", context)


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

# def employee_form(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('../profile/')
#         else:
#             return render(request, 'register/employee_form.html', {'form': form})
#     else:
#         form = EmployeeForm()
#         return render(request, 'register/employee_form.html', {'form': form})


def signin(request):

    if request.method == 'POST':
        login_data = Employee.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        # print("myoutput", username+password)
        isLoginTrue = 0
        user_data = 0

        for ldata in login_data:
            if (ldata.username == username) and (ldata.password == password):
                isLoginTrue = 1
                user_data = ldata
        if (isLoginTrue == 1) and (user_data != 0) and (user_data.user_type_id == 1):
            return render(request, "profile.html", {'ldata': login_data})
        elif (isLoginTrue == 1) and (user_data != 0) and (user_data.user_type_id == 2):
            return render(request, "admin_profile.html", {'ldata': login_data})
        else:
            return HttpResponse('user detail wrong')


def profile(request):
    return render(request, 'profile.html')


def admin_profile(request):
    return render(request, 'admin_profile.html')


def success(request):
    return render(request, 'success.html')


def signout(request):
    logout(request)
    return redirect('/')
