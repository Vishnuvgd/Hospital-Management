from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def department(request):
    doc_dept={
        'dept':departmentmodel.objects.all()
    }
    return render(request,'departments.html',doc_dept)

def doctors(request):
    a=doctorsmodel.objects.all()
    id=[]
    im=[]
    dn=[]
    dp=[]
    ds=[]
    for i in a:
        z=i.doc_img
        im.append(str(z).split('/')[-1])
        v=i.doc_name
        dn.append(v)
        e=i.id
        id.append(e)
        r=i.dept_name
        dp.append(r)
        x=i.doc_spec
        ds.append(x)
    mylist=zip(id,im,dn,dp,ds)
    return render(request,'doctors.html',{'mylist':mylist})

# def booking(request):
#     form=Bookingform()
#     dic_form={
#         'bform':form
#     }
#     return render(request,'booking.html',dic_form)

def booking(request):
    if request.method=='POST':
        a=bookingform(request.POST)
        if a.is_valid():
            pn=a.cleaned_data['p_name']
            ph=a.cleaned_data['p_phone']
            em=a.cleaned_data['p_email']
            dn = a.cleaned_data['doc_name']
            bk=a.cleaned_data['booking_date']
            b=bookingmodel(p_name=pn,p_phone=ph,p_email=em,doc_name=dn,booking_date=bk)
            b.save()
            return HttpResponse("booking success")
        else:
            return HttpResponse("failed..")
    return render(request,'booking.html')
