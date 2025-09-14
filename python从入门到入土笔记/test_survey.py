from survey import AnonymousSurvey

def test_store_single_response():
    """测试单个答案会被妥善地存储"""
    question = "What question did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('Chinese')
    assert 'Chinese' in language_survey.responses

def test_store_three_responses():
    """测试三个答案是否会被妥善保存"""
    question = "What question did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Chinese']
    for response in responses:
        language_survey.store_response(question)

    for response in responses:
        assert question in language_survey.responses

