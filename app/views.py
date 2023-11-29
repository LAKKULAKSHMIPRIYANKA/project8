from django.shortcuts import render

# Create your views here.

def carousel1(request):
    return render(request,'carousel1.html')



def carousel2(request):
    return render(request,'carousel2.html')


def carousel3(request):
    return render(request,'carousel3.html')