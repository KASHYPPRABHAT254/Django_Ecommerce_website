from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userform
from news.models import News
from django.core.mail import send_mail
def index(request):
    send_mail(
        'Testing mail',
        'hello prabhat kashyap',
        ['rishichabbra149@gmail.com'],
        fail_silently=False,
    )
    newsData=News.objects.all()
    data={
        'newsData':newsData
    }
    return render(request,"index.html",data)
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def news(request):
    return render(request,"news.html")
def footer(request):
    return render(request,"footer.html")
def navigationbar(request):
    return render(request,"navigationbar.html")
def submitform(request):
    if request.method=="POST":
        n1=int(request)
    return HttpResponse(request)
def loginform(request):
    output = 0
    uf=userform()
    data = {'form':uf}
    try:
        if request.method=="POST":
            #n1 = int(request.POST.get('num1'))
            #n2 = int(request.POST.get('num2'))
            #output = n1 + n2
            data = {
                #n1':n1,
                #'n2':n2,
                'output':output,
                'form':uf
            }
            url="/about/?output={}".format(output)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"loginform.html",data)
def calculator(request):
     c=''
     try:
         if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
     except:
         c="invalid opr...."
     print(c)
     return render(request,"calculator.html",{'c':c})
def evenodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="EVEN  NUMBER"
        else:
            c="ODD NUMBER"
    return render(request,"evenodd.html",{'c':c})
def newsDetails(request,newsid):
    newsDetails=News.objects.get(id=newsid)
    return render(request,"newsDetails.html")
 
