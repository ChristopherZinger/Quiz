import string
import random

def code_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create unique code for user
def create_shortcode(instance, size=10):
    new_code = 'code={}'.format(code_generator(size=size))
    myClass = instance.__class__
    qs_exists = myClass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size = size)
    return new_code

# Genereate question set for each game
def generate_question_set(instance, questionClass, nr_of_questions=5):
    # Create list with all available quesion ids
    list_id = []
    for i in questionClass.objects.all():
        list_id.append(i.id)

    # choose random set of questions
    question_set_id = []
    for i in range(nr_of_questions):
        choice = random.choice(list_id)
        question_set_id.append(choice)
        list_id.remove(choice) #remove id forom list to avoid duplication of the question in the set

    return question_set_id
