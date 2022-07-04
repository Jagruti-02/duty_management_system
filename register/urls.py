from django.urls import path,include
from . import views

urlpatterns = [
    #get and post req for insert
    path('',views.employee_form,name='employee_insert'),

    #get and post req for update
    path('<int:id>/',views.employee_form,name='employee_update'),

    #get req to retrieve  and display all records
    path('list/',views.employee_list,name='employee_list'),

    #delete operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),


]
