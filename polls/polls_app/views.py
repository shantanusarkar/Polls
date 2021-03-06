from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from polls_app.models import Poll, Choice
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
            pub_date__lte = timezone.now()
            ).order_by('-pub_date')[:5]

def home(request):
    return render(request, 'home.html')

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'detail.html'

    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Poll
    template_name = 'results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'poll' : p,
            'error_message' : "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))

def add(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    selected_choice = p.choice_set.get(pk = request.POST['choice'])
    selected_choice.choice_set.create(choice_text = message, votes = 0)

