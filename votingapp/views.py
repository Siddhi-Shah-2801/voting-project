from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
arr= ['Java','Python','C++','C','ASP.Net','JavaScript','PHP','Swift','SQL','MYSQl','Flutter','Dart','Objective C','MATLAB','R','Ruby','Go','React','Perl','VisualBasic','Html','Css']
globalcount = dict()
def index(request):
    mydictionary={
        "arr":arr
    }
    return render (request,'index.html',context=mydictionary)
def getquery(request):
    q=request.GET['languages']
    if q in globalcount:
        # if already exist then increment the value
       globalcount[q]=globalcount[q]+1
    else:
       # First Occurence
       globalcount[q]=1 
    mydictionary={
        "arr":arr,
        "globalcount" :globalcount
    }
    return render(request,'index.html',context=mydictionary)
def sortdata(request):
   global globalcount
   globalcount=dict(sorted(globalcount.items(),key=lambda x:x[1],reverse=True))
   mydictionary={
        "arr":arr,
        "globalcount" :globalcount
    } ;return render(request,'index.html',context=mydictionary)