from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'Syeraa','id':'007'}
    return render(request,'jinja.html',context=d)

def condition(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'condition.html',context=d)

def loop(request):
    # d={'name':''}
    d={'name':'SSS'}
    return render(request,'loop.html',d)