from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render
from polls_app.models import Poll
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'index.html', context)

def home(request):
    return HttpResponse("Hello EveryOne!")

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'poll' : poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)