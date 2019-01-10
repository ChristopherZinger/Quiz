from django import forms
from .models import Question, Player


class QuestionCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Question
        fields = [
            'title',
            'question',
            'question_img',
            'correct_answer',
            'answer_A',
            'answer_B',
            'answer_C',
            'answer_D',
            'answer_A_img',
            'answer_B_img',
            'answer_C_img',
            'answer_D_img',

        ]

class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
        ]
