from django.shortcuts import render, redirect  
from .forms import CreateForm, CreateVacForm
from .models import Patient, Vaccine
from django.core.exceptions import MultipleObjectsReturned
from django.contrib import messages

def add(request):  
    if request.method == "POST":  
        form = CreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CreateForm()  
    return render(request,'main/index.html',{'form':form})

def vacadd(request, id):
    patient = Patient.objects.get(id=id)
    vaccines = Vaccine.objects.filter(patient_id=patient.id)
    num = vaccines.count()
    print("num is")
    print(num)
    if num < 4:
        print("less then 4")
        if request.method == "POST":  
            form = CreateVacForm(request.POST) 

            if form.is_valid():  
                try:  
                    form.save() 
                    return redirect('/show')  
                except:  
                    pass  
        else:  
            form = CreateVacForm() 
        return render(request,"main/addVac.html",{'form':form ,'patient':patient} )
    else:
        print("more then 4")
        messages.warning(request, "This Patient was 4444444444 Vaccines already")
        return redirect("/show" , massege="This Patient was 4 Vaccines already")

def show(request):  
    patients = Patient.objects.all()  
    return render(request,"main/show.html",{'patients':patients}) 

def vacshow(request, id):  
    patient = Patient.objects.get(id=id)
    vaccines = Vaccine.objects.filter(patient_id=patient.id)
    return render(request,"main/vacshow.html",{'vaccines':vaccines , 'id':id}) 

def edit(request, id):  
    patient = Patient.objects.get(id=id)  
    return render(request,'main/edit.html', {'patient':patient})

def update(request, id):  
    patient = Patient.objects.get(id=id)  
    form = CreateForm(request.POST, instance = patient)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'main/edit.html', {'patient': patient})

def destroy(request, id):  
    patient = Patient.objects.get(id=id)  
    patient.delete()  
    return redirect("/show") 

