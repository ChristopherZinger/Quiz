
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from .forms import QuestionCreateForm, PlayerCreateForm
from .models import Question, Player

# ---------------- Quiz Question CRUD ----------------------
# Create Delete Update Detail Views
class QuestionCreateView(CreateView):
    template_name = 'question/create.html'
    form_class = QuestionCreateForm
    queryset = Question.objects.all()


class QuestionDeleteView(DeleteView):
    template_name = 'question/delete.html'
    model = Question

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Question, id=id)

    def get_success_url(self):
        return reverse('quizgame:list')


class QuestionDetailView(DetailView):
    template_name = 'question/detail.html'
    queryset = Question.objects.all()

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Question, id=id)


class QuestionUpdateView(UpdateView):
    template_name = 'question/create.html'
    form_class = QuestionCreateForm
    model = Question
    queryset = Question.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Question, id=id_)


class QuestionListView(ListView):
    model = Question
    template_name = 'question/list.html'
    queryset = Question.objects.all()


# ---------------- Quiz Views ----------------------


class PlayerReviewView(TemplateView):
    template_name = 'quizgame/review.html'
    def get_context_data(self, **kwargs):
        context = super(PlayerReviewView, self).get_context_data(**kwargs)
        shortcode = self.kwargs.get('player_shortcode')
        questions = Player.objects.get(shortcode=shortcode).questions.all()
        context['questions'] = questions
        print(context)
        return context


class PlayerCreateView(CreateView):
    template_name = 'quizgame/player_create.html'
    form_class = PlayerCreateForm
    model = Player
    queryset = Player.objects.all()


class QuizIndexView(TemplateView):
    template_name = 'quizgame/index.html'

class QuizResultsView(TemplateView):
    template_name = 'quizgame/result.html'

    # equivalen of get_context_data function
    def players(self):
        return Player.objects.all().order_by('-time_points')[:5]

    def get_context_data(self, **kwargs):
        context = super(QuizResultsView, self).get_context_data(**kwargs)
        shortcode = self.kwargs.get('player_shortcode')

        # player score
        context['player_score'] = Player.objects.get(shortcode=shortcode).time_points
        context['correct_answer'] = Player.objects.get(shortcode=shortcode).points
        context['shortcode'] = shortcode
        return context


class QuizQuestionView(TemplateView):
    template_name = 'quizgame/quiz.html'

class AboutView(TemplateView):
    template_name = 'quizgame/about.html'

class AuthorView(TemplateView):
    template_name = 'quizgame/author.html'
