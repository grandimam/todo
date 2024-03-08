from models import Question
from forms import QuestionForm
from django.views.generic import ListView
from django.views.generic import DetailView


class QuestionListingView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question
    form_class = QuestionForm
    template_name = "detail.html"
