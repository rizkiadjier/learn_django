from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib import messages
from crudapplication.models import Employee
from .forms import EmployeeForm

# Create your views here.
def emp(request):
    return render(request, "index.html")

def show(request):
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Employee.objects.all()
         
    return render(request, "show.html", context)

def edit(request, id):
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Employee.objects.get(id=id)

    return render(request, 'edit.html', context)

def update(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Employee, id = id)
 
    # pass the object as instance in form
    form = EmployeeForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    #context["form"] = form
    context["dataset"] = Employee.objects.all()
 
    return render(request, "show.html", context)

def delete(request):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Employee, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "show.html", context)