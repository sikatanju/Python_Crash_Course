import pytest
from anonymous_survery import AnonymousSurvery

# *** Simple test on one and three languages:

# def test_one_language():
#     language_survey = AnonymousSurvery(" ")
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# def test_three_languages():
#     language_survey = AnonymousSurvery(" ")
#     languages = ['English', 'Bengali', 'Spanish']
#     language_survey.store_response('English')
#     language_survey.store_response('Bengali')
#     language_survey.store_response("Spanish")
#     for language in languages:
#         assert language in language_survey.responses


# *** Using simplest fixture for one test: 

@pytest.fixture
def language_survey_obj():
    language_survey_obj = AnonymousSurvery("What language did you learn to speak first: ")
    return language_survey_obj

# * By using the same obj name in the test function and fixture function, we're calling the fixture function to get that object
def test_three_languages(language_survey_obj):
    # language_survey = AnonymousSurvery(" ")
    languages = ['English', 'Bengali', 'Spanish']
    language_survey_obj.store_response('English')
    language_survey_obj.store_response('Bengali')
    language_survey_obj.store_response("Spanish")
    for language in languages:
        assert language in language_survey_obj.responses
