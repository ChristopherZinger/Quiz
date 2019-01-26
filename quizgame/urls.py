from django.conf.urls import url, include
from .views import (
    AboutView,
    AuthorView,
    PlayerCreateView,
    PlayerReviewView,
    QuestionCreateView,
    QuestionDeleteView,
    QuestionDetailView,
    QuestionListView,
    QuestionUpdateView,
    QuizIndexView,
    QuizQuestionView,
    QuizResultsView,
    )
from django.views.generic import TemplateView

app_name = 'quizgame'

# url = ^quizgame/...
urlpatterns = [

    # Quiz Question Manager
    url(r'^question/create/$',              QuestionCreateView.as_view(),   name='create'),
    url(r'^question/(?P<pk>\d+)/delete/$',  QuestionDeleteView.as_view(),   name='delete'),
    url(r'^question/(?P<pk>\d+)/$',         QuestionDetailView.as_view(),   name='detail'),
    url(r'^question/list/$',                QuestionListView.as_view(),     name='list'),
    url(r'^question/(?P<pk>\d+)/update/$',  QuestionUpdateView.as_view(),   name='update'),

    # Quiz Game URLS
    url(r'^index/$', QuizIndexView.as_view(), name='index'),
    url(r'^create_player/$', PlayerCreateView.as_view(), name='create_player'),
    url(r'^game/(?P<player_shortcode>[\w=]+)/$', QuizQuestionView.as_view(), name='question'),
    url(r'^results/(?P<player_shortcode>[\w=]+)/$', QuizResultsView.as_view(), name='results'),
    url(r'^review/(?P<player_shortcode>[\w=]+)/$', PlayerReviewView.as_view(), name='review'),
    url(r'^author/$', AuthorView.as_view(), name='author'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    # API
    url(r'^api/', include('quizgame.api.urls', namespace='api')),
]
