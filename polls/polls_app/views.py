from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def home(request):
    return render_to_response('index.html')

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)