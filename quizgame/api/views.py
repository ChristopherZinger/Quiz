from collections import OrderedDict
import json
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from quizgame.models import Question, Player
from .serializers import (
    CorrectAnswerSerializer,
    NextImgQuestionSerializer,
    NextQuestionSerializer,
    PlayerDetailPointsSerializer,
    QuestionListSerializer,
    QuestionDetailSerializer,
    QuestionPlayerSerializer,
    )
from random import randint
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse

class GetPlayersChartAPIView(APIView):
    def get(self, request, format=None):
        # get all the players
        players = Player.objects.all()
        players_list = []

        # prepare player data list for precize chart
        # for i in players:
        #     players_list.append([i.time_points])

        # prepare player data list for rounded chart
        for i in players:
            players_list.append([round(i.time_points/10)*10])
        # group players by score for chart
        od = OrderedDict()
        for sub in players_list:
            od.setdefault(sub[0],[]).append(sub)
        # stringify and return response
        json_data = json.dumps(od)
        return Response(json_data)



class QuestionAPIListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


# class QuestionAPIDetailView(RetrieveAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionDetailSerializer


class QuestionEvaluateAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):

        # Get player object
        shortcode = self.kwargs['player_shortcode']
        player = Player.objects.get(shortcode=shortcode)
        if player.current_status == '(\'open\', \'open\')' :
            # return context - id of quiesiton to be asked
            player.set_next_question()
            #check if question have a img
            if player.current_question_obj.question_img:
                serializer = NextImgQuestionSerializer(player.current_question_obj, context={"request":request})
                return Response(serializer.data)
            else:
                serializer = NextQuestionSerializer(player.current_question_obj)
                return Response(serializer.data)
        return Response({'status':'closed'})

    def post(self, request, format=None, *args, **kwargs):
        # feth request data
        answer = request.data['answer_id']
        question_id = request.data['question_id']
        time = request.data['time']
        # feth player from database
        shortcode = self.kwargs['player_shortcode']
        player = Player.objects.get(shortcode=shortcode)
        # get question
        question = Question.objects.get(id=question_id)
        # check if answer is correct
        if question.correct_answer == answer:
            # Get player objects
            time_points = int(time)
            player.add_points(time_points)
        #check how many question remains
        remain_questions_nr = player.questions.count() - player.current_question_nr + 1
        return Response({'remain_questions_nr': remain_questions_nr, 'status':player.current_status})


# view decides whith anwser should be correct when creating new Quiesion
# it finds least quantity of A B C or D
class GenerateCorrectAnswerAPIDetailView(APIView):
    def get(self, request, format=None):
        # Get objects by correct answers
        A = Question.objects.filter(correct_answer='A')
        B = Question.objects.filter(correct_answer='B')
        C = Question.objects.filter(correct_answer='C')
        D = Question.objects.filter(correct_answer='D')

        # find least popular awser
        myArray = [A, B, C, D]
        myArrayNrs = [A.count(), B.count(), C.count(), D.count()]

        # return context
        correct_answer_to_serialize = myArray[myArrayNrs.index(min(myArrayNrs))][0]
        serializer = CorrectAnswerSerializer(correct_answer_to_serialize)
        return Response(serializer.data)



class PlayerAPIDetailView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        # Get object
        shortcode = self.kwargs['player_shortcode']
        obj = Player.objects.get(shortcode=shortcode)

        # return context
        serializer = QuestionPlayerSerializer(obj)
        return Response(serializer.data)


class NextQuestionAPIDetailView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        # Get object
        shortcode = self.kwargs['player_shortcode']
        obj = Player.objects.get(shortcode=shortcode)
        obj.set_next_question()

        # return context - id of quiesiton to be asked
        serializer = NextQuestionSerializer(obj.current_question_obj)
        return Response(serializer.data)






# ---
