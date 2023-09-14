from django.shortcuts import render
import datetime
# Create your views here.

def built_in_filters(request):
    data='My NAme IS shaShi vARdhan'
    date=datetime.datetime.now()
    d={'data':data,'date':date ,'c':13}
    return render (request,'built_in_filters.html',d)