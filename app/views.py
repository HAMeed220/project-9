from django.shortcuts import render

# Create your views here.

def data_render (request):
    data='This data is our Assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)

def login(request):

    d={'username':'Hameed','Age':22,'degree':'B Tech'}
    return render(request,'login.html',context=d)
