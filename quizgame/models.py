from django.db import models
from django.urls import reverse
from .utils import create_shortcode, generate_question_set

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=150)
    question = models.CharField(max_length=1000)

    answer_A = models.CharField(max_length=100)
    answer_B = models.CharField(max_length=100)
    answer_C = models.CharField(max_length=100)
    answer_D = models.CharField(max_length=100)

    player_answer_A = models.IntegerField(default=0)
    player_answer_B = models.IntegerField(default=0)
    player_answer_C = models.IntegerField(default=0)
    player_answer_D = models.IntegerField(default=0)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

    anwsers = (
        ( A , answer_A),
        ( B , answer_B),
        ( C , answer_C),
        ( D , answer_C),
    )
    correct_answer = models.CharField( max_length=1, choices=anwsers, default=A )

    question_img = models.ImageField(upload_to='question/', null=True, blank=True, default=None)

    answer_A_img = models.ImageField(upload_to='question/', null=True, blank=True)
    answer_B_img = models.ImageField(upload_to='question/', null=True, blank=True)
    answer_C_img = models.ImageField(upload_to='question/', null=True, blank=True)
    answer_D_img = models.ImageField(upload_to='question/', null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quizgame:list')


# in this model you can decide how many quesions player will receive
class Player(models.Model):

    name                    = models.CharField(max_length=100)
    shortcode               = models.CharField(max_length=15, unique=True)
    questions               = models.ManyToManyField(Question, related_name='question_set')
    current_question_nr     = models.IntegerField(default=0)
    current_question_obj    = models.ForeignKey(Question, related_name='current_question', blank=True, null=True, default=None)
    time_points             = models.IntegerField(default=0)
    points                  = models.IntegerField(default=0) # this should be named correct_answers
    nr_of_questions         = models.IntegerField(default=10)
    pending = 'pending'
    open = 'open'
    closed = 'closed'
    status = (
        (pending, 'pending'),
        (open, 'open'),
        (closed, 'closed'),
    )
    current_status = models.CharField( max_length=7, choices=status, default=pending )

    def __str__(self):
        return ("{} - {}".format(self.name, self.shortcode))

    def get_absolute_url(self):
        return reverse('quizgame:question', kwargs={'player_shortcode':self.shortcode})

    def save(self, *args,**kwargs):
        #generate individual code for player
        if self.shortcode is None or self.shortcode == "" :
            self.shortcode = create_shortcode(self)
        #save
        super(Player, self).save(*args, **kwargs)
        #generate question set for a player
        if self.questions.all().count() == 0:
            questions_ids = generate_question_set(self, Question, self.nr_of_questions)
            for id in questions_ids:
                self.questions.add(Question.objects.get(id=id))
                self.current_status = self.status[1]
                self.save(update_fields=['current_status'])

    def set_next_question(self):
        # check if all the quesions were already asked
        if self.current_question_nr >= (self.nr_of_questions):
            self.current_status = self.status[2]
            self.save(update_fields=['current_status'])
        else:
            # get question
            id = self.questions.all()[self.current_question_nr].id
            self.current_question_obj = self.questions.get(id=id)
            # update current question number
            print('Question ID : {}, \n Question number : {}'.format(self.current_question_obj.id, self.current_question_nr))
            self.current_question_nr += 1
        self.save()

    def add_points(self,time_points):
        self.points +=1
        self.time_points += time_points
        self.save()
        print('points in model : {}'.format(self.points))
