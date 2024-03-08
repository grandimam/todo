from django.urls import path
from views import QuestionDetailView

urlpatterns = [
    path('detail/', QuestionDetailView.as_view()),
]
