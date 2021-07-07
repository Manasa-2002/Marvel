from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import ContactcarrersForm, ContactprojectsForm, ContactservicesForm
from .models import Contactcarrers,Contactprojects,Contactservices,Video
# Create your views here.
def contactcarrers_view(request):
    form=ContactcarrersForm()
    if request.method=="POST":
        form=ContactcarrersForm(request.POST)
        if form.is_valid():
            form.save()
            form.save() 
            return redirect('marmag')
    return render(request,'MarvelApp/contactcarrers.html',{'form':form})	

def contactprojects_view(request):
    form=ContactprojectsForm()
    if request.method=="POST":
        form=ContactprojectsForm(request.POST)
        if form.is_valid():
            form.save()
            form.save() 
            return redirect('marmag')
    return render(request,'MarvelApp/contactprojects.html',{'form':form})

def contactservices_view(request):
    form=ContactservicesForm()
    if request.method=="POST":
        form=ContactservicesForm(request.POST)
        if form.is_valid():
            form.save()
            form.save() 
            return redirect('marmag')
    return render(request,'MarvelApp/contactservices.html',{'form':form})

def home_view(request):
    return render(request,'MarvelApp/home.html')

def service_view(request):
    return render(request,'MarvelApp/Services.html')

def project_view(request):
    return render(request,'MarvelApp/projects.html')

def aboutus_view(request):
    return render(request,'MarvelApp/aboutus.html')

def archieture_view(request):
    return render(request,'MarvelApp/Archieture.html')

def drafting_view(request):
    return render(request,'MarvelApp/Drafting.html')

def engineering_view(request):
    return render(request,'MarvelApp/Engineering.html')

def valueadded_view(request):
    return render(request,'MarvelApp/Value Added.html')

def commercialp_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/commercialp.html',{"video":video})

def industrialp_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/industrialp.html',{"video":video})

def infrastructurep_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/infrastructurep.html',{"video":video})

def oilgasp_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/oilgasp.html',{"video":video})

def powerp_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/powerp.html',{"video":video})

def specialp_view(request):
    video=Video.objects.all()
    return render(request,'MarvelApp/specialp.html',{"video":video})

