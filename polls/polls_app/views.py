from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from polls_app.models import Poll
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
def home(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ','.join([p.question for p in latest_poll_list ])
    return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)