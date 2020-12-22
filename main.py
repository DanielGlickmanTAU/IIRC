import json
import random

dev_json = open('dev.json').read()
dev = json.loads(dev_json)

def random_question(questions):
    q = random.choice(questions)
    q = random.choice(q['questions'])

    try:
        answers = ' | '.join([x['text'] for x in q['answer'].get('answer_spans')])
        question = q['question']
        links = ' | '.join(q['question_links'])
    except Exception as e:
        print(e)
        print(q)

    return {'question':question ,'links': links, 'answer':answers}

def pretty_print(question):
    print(
        'question : ' + question.get('question') + '\n'
        + 'links : ' + question.get('links') + '\n'
        + 'answer : ' + question.get('answer')

    )


def get_question(questions, question_text):
    return next(q for q in questions if question_text in str(q))

