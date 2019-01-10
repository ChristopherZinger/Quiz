from rest_framework.serializers import ModelSerializer, SerializerMethodField
from quizgame.models import Question, Player




class CorrectAnswerSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['correct_answer',]


class NextImgQuestionSerializer(ModelSerializer):
    img_url =  SerializerMethodField()
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'question',
            'img_url',
            'answer_A',
            'answer_B',
            'answer_C',
            'answer_D',
        ]
    def get_img_url(self, question):
        request = self.context.get('request')
        img_url = question.question_img.url
        return request.build_absolute_uri(img_url)


class NextQuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'question',
            'answer_A',
            'answer_B',
            'answer_C',
            'answer_D',
        ]



class PlayerDetailPointsSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'points',

        ]


class QuestionDetailSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
            'question',
            'answer_A',
            'answer_B',
            'answer_C',
            'answer_D',
        ]

class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'question',
            'answer_A',
            'answer_B',
            'answer_C',
            'answer_D',
        ]

class QuestionPlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'name',
            'shortcode',
            'current_status',
            'current_question',
            'questions',
        ]
