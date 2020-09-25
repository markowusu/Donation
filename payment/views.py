from django.shortcuts import render

# Create your views here.

def index(request):

    if 2==2:
        pass

    return render(request,'payment/index.html')