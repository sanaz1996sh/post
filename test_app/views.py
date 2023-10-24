from django.shortcuts import render
from .models import *

# Create your views here.
def contact(request):
    n=request.POST.get("name")
    e=request.POST.get("email")
    m=request.POST.get("message")
    if(n and e and m):
       contactcls.objects.create(name=n,email=e,message=m)
       return render(request,"test_app/message.html")
     
    return render(request,"test_app/contact.html")