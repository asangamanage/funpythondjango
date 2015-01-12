from django.shortcuts import render_to_response

from django.http import HttpResponse

def index(request):
    returnUrl = request.GET.get('returnUrl', '')
    return render_to_response('index.html',{'returnUrl': returnUrl})
