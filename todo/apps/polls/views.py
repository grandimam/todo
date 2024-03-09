from .models import Poll
from .models import Choice, Question
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView


class PollDetailView(DetailView):
    model = Poll
    template_name = 'detail.html'
    context_object_name = 'poll'

    def post(self, request, *args, **kwargs):
        poll_id = self.kwargs['pk']
        poll_obj = Poll.objects.get(id=poll_id)
        question = Question.objects.get(id=poll_obj.question.id)
        choice_id = request.POST.get('choice')
        choice = Choice.objects.get(id=choice_id)
        choice.votes += 1
        choice.save()
        return render(request, 'result.html', {'question': question})


class PollListingView(ListView):
    model = Poll
    template_name = 'listing.html'
    context_object_name = 'poll_listing'

    def get_queryset(self):
        return Poll.objects.filter(is_active=True)
