from survey import AnonymousSurvey

def test_store_single_response():
    """testa se uma única resposta está devidamente armazenada"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses():
    """Testa se três respostas individuais estão devidamente armazenadas"""
    question = "What language did you first learn to speak?"
    language_surgey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']

    for response in responses:
        language_surgey.store_response(response)


    for response in responses:
        assert response in language_surgey.responses

@pytest.fixture
def language_survey():
    "Uma pesquisa que estará disponivel para todas a funções de teste"
    question = "What language did you learn to speak?"

    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_responde(language_survey):
    """Testa se uma unica resposta está devidamente armazenada"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Testa se três respostas individuais estão devidamente armazenadas"""
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

