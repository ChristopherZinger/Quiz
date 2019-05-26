from django.conf.urls import url
from .views import (
GetPlayersChartAPIView,
    NextQuestionAPIDetailView,
    PlayerAPIDetailView,
    QuestionEvaluateAPIView,
    QuestionAPIListView,
    # QuestionAPIDetailView,
    GenerateCorrectAnswerAPIDetailView,

)

app_name = 'api'
# url = ^quizgame/api/...
urlpatterns = [
    # url(r'^(?P<pk>\d+)/evaluate/$', QuestionEvaluateAPIView.as_view()),
    url(r'^generate_correct_answer/$', GenerateCorrectAnswerAPIDetailView.as_view(), name='correct_answer'),
    url(r'^list/$', QuestionAPIListView.as_view(), name='list'),
    url(r'^get_players_chart/$', GetPlayersChartAPIView.as_view(), name='players_chart'),
    # url(r'^(?P<pk>\d+)/$', QuestionAPIDetailView.as_view(), name='detail'),
    url(r'^(?P<player_shortcode>[\w=]+)/$', PlayerAPIDetailView.as_view(), name='player'),
    # url(r'^(?P<player_shortcode>[\w=]+)/questions/$', NextQuestionAPIDetailView.as_view()),
    url(r'^(?P<player_shortcode>[\w=]+)/questions/$', QuestionEvaluateAPIView.as_view()),

    #url(r'^(?P<pk>\d+)/evaluate/$', QuestionEvaluateAPIView.as_view(), name='evaluate'),




]
