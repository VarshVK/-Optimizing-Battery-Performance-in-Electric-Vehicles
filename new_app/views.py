from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import predict






# Create your views here.
# Create your views here.  
def home(request):
	return render(request,'index.html')


def input(request):
    return render(request,'input.html')
        

def output(request):
	algo=request.POST.get('algo')
	row=int(request.POST.get('row'))
	out=predict(algo,row)
	print(out[0])
	classes = float(out[0])

	print(classes)
	return render(request,'output.html',{'out':classes})
