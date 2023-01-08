from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    rf=RegistrationForm()
    pf=Profile()
    d={'rf':rf,'pf':pf}
    if request.method=='POST' and request.FILES:
        UD=RegistrationForm(request.POST)
        PD=Profile(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            pw=UD.cleaned_data['password']
            USO=UD.save(commit=False)
            USO.set_password(pw)
            USO.save()
            PFO=PD.save(commit=False)
            PFO.user=USO
            PFO.save()

            send_mail('Registration details','Registration Successfull','rsu191912@gmail.com',[USO.email],fail_silently=False)
            return HttpResponse('registration Successfull')

    return render(request,'registration.html',d)