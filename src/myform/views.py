from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactModel
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import checksum
import random
# Create your views here.
MERCHANT_KEY='Mh5!V!1fN5bUOIIY'
def contact_view(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('number') and request.POST.get('workshops') :
            contact = ContactModel()
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.number = request.POST.get('number')
            contact.workshops = request.POST.get('workshops')
            contact.save()
            #request paytm to tranfer the amount to your account after payment by user
            param_dict={
                'MID':'kQjgVH56416757844055',
                'ORDER_ID': str(random.random()*100000),
                'TXN_AMOUNT': '100',
                'CUST_ID': 'nehaparmar1899@gmail.com',
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
            }
            param_dict['CHECKSUMHASH']=checksum.generate_checksum(param_dict,MERCHANT_KEY)

            return render(request, "paytm.html", {'param_dict':param_dict})
        return render(request,"index.html",{})
    else:
        return render(request,"index.html",{})

#def home(request):
 #   return render(request,"other.html",{})
 #decorator-chhanges functionality of function
@csrf_exempt
def handlerequest(request):
    '''
    form=request.POST
    response_dict={}
    for i in form.keys():
        response.dict[i]=form[i]
        if i=='CHECKSUMHASH':
            checksum=form[i]

    verify=checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPONSE']=='01':
            print("Order successful")
        else:
            print("Order not successful because"+ response_dict['RESPMSG'])
    return render(request,'myform/paymentstatus.html',{'response':response_dict})
    '''
    return HttpResponse('done')
    pass
    #paytm will send you post request heretherefore it should be exempted from csrf