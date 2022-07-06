from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from matplotlib.style import context
from .forms import EmployeeForm
from .models import Employee, report_table
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
    return redirect('/adminprofile')


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
            return render(request, "profile.html", {'ldata': username})
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


def assign(request):
    login_data = Employee.objects.all()
    reportings = report_table.objects.all()
    d = {}
    for i in reportings:
        date = i.date
        if date in d:
            d[date].append(i.emp_code)
        else:
            d[date] = [i.emp_code]
    return render(request, 'assign.html', {'ldata': login_data, 'reportings': d})

def reporting(request):
    return render(request, 'reporting.html')

def addtask(request):
    if request.method == "POST":
        drop1 = request.POST['drop1']
        drop2 = request.POST['drop2']
        drop3 = request.POST['drop3']
        drop4 = request.POST['drop4']
        drop5 = request.POST['drop5']
        date = request.POST['date']
        if drop1 != "Select ID":
            data = report_table(emp_code=drop1, date=date)
            data.save()
        if drop2 != "Select ID":
            data2 = report_table(emp_code=drop2, date=date)
            data2.save()

        if drop3 != "Select ID":
            data3 = report_table(emp_code=drop3, date=date)
            data3.save()
        if drop4 != "Select ID":
            data4 = report_table(emp_code=drop4, date=date)
            data4.save()
        if drop5 != "Select ID":
            data5 = report_table(emp_code=drop5, date=date)
            data5.save()
    return HttpResponseRedirect(reverse('assign'))

def signout(request):
    logout(request)
    return redirect('/')
