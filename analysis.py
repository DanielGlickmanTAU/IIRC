def text_len(sample):
    return len(sample['text'])


def question_len(question):
    return len(question['question'])


def context_len(question):
    return sum([len(q['text']) for q in question['context'] if q['passage'] != 'main'])


def random_question(questions):
    q = random.choice(questions)
    q = random.choice(q['questions'])

    try:
        answers = ' | '.join([x['text'] for x in q['answer'].get('answer_spans')])
        question = q['question']
        links = ' | '.join(q['question_links'])
        return {'question': question, 'links': links, 'answer': answers}
    except Exception as e:
        print(e)
        print(q)


def pretty_print(question):
    print(
        'question : ' + question.get('question') + '\n'
        + 'links : ' + question.get('links') + '\n'
        + 'answer : ' + question.get('answer')

    )


def get_question(questions, question_text):
    return next(q for q in questions if question_text in str(q))


def get_questions_by_predicate(questions, pred):
    def _type_pred(q, type='numerical'):
        return q['answer'].get('type') == type

    return [q for q in questions if pred(q)]
