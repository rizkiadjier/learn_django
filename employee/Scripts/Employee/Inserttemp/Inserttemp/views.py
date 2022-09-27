from django.shortcuts import render
from Inserttemp.models import EmpInsert
from django.contrib import messages

def InsertRecord(request):
    if request.method == 'POST':
        if(request.POST.get('empName') and request.POST.get('empEmail') and request.POST.get('empCountry')):
            saveRecord = EmpInsert()
            saveRecord.emp_name = request.POST.get('empName')
            saveRecord.email = request.POST.get('empEmail')
            saveRecord.country = request.POST.get('empCountry')
            saveRecord.save()
            return render(request, 'Index.html')
        else:
            return render(request, 'Index.html')