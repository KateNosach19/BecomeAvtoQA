import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-avto')
    
    assert r['total_count'] == 1
    assert 'BecomeAvtoQA' in r['items'][0]['name']
   
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_wiht_one_char_be_found(github_api):
    r = github_api.search_repo('a')  
    assert r['total_count'] != 0
