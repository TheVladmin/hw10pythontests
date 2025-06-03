from faker import Faker
from pytest_steps import test_steps
fake = Faker()
from modules.goals_methods import create_goal2, get_goals, delete_goal1, delete_goal2, create_goal1, \
    get_goals_invalid_team_id, get_goals_invalid_token, get_goal, create_goal_invalid_tid, create_goal_invalid_token, \
    get_goal_invalid_lid, get_goal_invalid_token, update_goal, update_goal_invalid_gid, update_goal_invalid_token, \
    delete_goal_invalid_gid, delete_goal_invalid_token


# pytest --template=html1/index.html --report=report.html

## GET GOALS POSITIVE TESTS

@test_steps("GET GOALS / Create Goal 1", "GET GOALS / Create Goal 2", "GET GOALS / Get goals", "GET GOALS / Delete Goal 1","GET GOALS / Delete Goal 2")
def test_get_goals():
    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    result_create2 = create_goal2()
    goal_random_name2 = result_create2.json()['goal']['name']
    goal2_id = result_create2.json()['goal']['id']
    assert result_create2.status_code == 200
    assert result_create2.json()['goal']["name"] == goal_random_name2
    yield

    result_get_goals = get_goals()
    goal_random_name = result_get_goals.json()['goals'][0]['name']
    goal_random_name2 = result_get_goals.json()['goals'][1]['name']
    assert result_get_goals.status_code == 200
    assert result_get_goals.json()['goals'][0]['name'] == goal_random_name
    assert result_get_goals.json()['goals'][1]['name'] == goal_random_name2
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

    result_delete2 = delete_goal2(goal2_id)
    assert result_delete2.status_code == 200
    yield

## GET GOALS NEGATIVE TESTS

@test_steps("GET GOALS / Create Goal 1", "GET GOALS / Create Goal 2", "GET GOALS / Get goals / Invalid team ID","GET GOALS / Get goals / Invalid token", "GET GOALS / Delete Goal 1","GET GOALS / Delete Goal 2")
def test_get_goals_negative():
    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    result_create2 = create_goal2()
    goal_random_name2 = result_create2.json()['goal']['name']
    goal2_id = result_create2.json()['goal']['id']
    assert result_create2.status_code == 200
    assert result_create2.json()['goal']["name"] == goal_random_name2
    yield

    result_get_goals_invalid_t_id = get_goals_invalid_team_id()
    assert result_get_goals_invalid_t_id.status_code == 401
    assert result_get_goals_invalid_t_id.json()['err'] == "Team not authorized"
    assert result_get_goals_invalid_t_id.json()['ECODE'] == "OAUTH_060"
    yield

    result_get_goals_invalid_token = get_goals_invalid_token()
    assert result_get_goals_invalid_token.status_code == 401
    assert result_get_goals_invalid_token.json()['err'] == "Oauth token not found"
    assert result_get_goals_invalid_token.json()['ECODE'] == "OAUTH_019"
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

    result_delete2 = delete_goal2(goal2_id)
    assert result_delete2.status_code == 200
    yield


## CREATE GOAL POSITIVE TESTS

@test_steps("CREATE GOALS / Create new goal","CREATE GOALS / Get created goal", "CREATE GOALS / Delete created goal")
def test_create_goal():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## CREATE GOAL NEGATIVE TESTS

@test_steps("CREATE GOALS / Create new goal with invalid team ID","CREATE GOALS / Create new goal with invalid token", "CREATE GOALS / Get created goals")
def test_create_goal_negative():

    result_create_invalid_tid = create_goal_invalid_tid()
    assert result_create_invalid_tid.status_code == 401
    assert result_create_invalid_tid.json()['err'] == "Team not authorized"
    assert result_create_invalid_tid.json()['ECODE'] == "OAUTH_061"
    yield

    result_create_invalid_token = create_goal_invalid_token()
    assert result_create_invalid_token.status_code == 401
    assert result_create_invalid_token.json()['err'] == "Oauth token not found"
    assert result_create_invalid_token.json()['ECODE'] == "OAUTH_019"
    yield

    result_get_Goals = get_goals()
    assert result_get_Goals.status_code == 200
    assert result_get_Goals.json()['goals'] == []
    yield

## GET ONE GOAL POSITIVE TESTS

@test_steps("GET GOAL / Create new goal","GET GOAL / Get goal", "GET GOAL / Delete goal")
def test_get_goal():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## GET ONE GOAL NEGATIVE TESTS

@test_steps("GET GOAL / Create new goal","GET GOAL / Get goal with invalid goal ID", "GET GOAL / Get goal with invalid token","GET GOAL / Delete goal")
def test_get_goal_negative():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_invalid_lid_result = get_goal_invalid_lid()
    assert get_one_goal_invalid_lid_result.status_code == 401
    assert get_one_goal_invalid_lid_result.json()['err'] == "Team not authorized"
    assert get_one_goal_invalid_lid_result.json()['ECODE'] == "OAUTH_027"
    yield

    get_one_goal_invalid_token_result = get_goal_invalid_token(goal_id)
    assert get_one_goal_invalid_token_result.status_code == 401
    assert get_one_goal_invalid_token_result.json()['err'] == "Oauth token not found"
    assert get_one_goal_invalid_token_result.json()['ECODE'] == "OAUTH_019"
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## UPDATE GOAL POSITIVE TESTS

@test_steps("UPDATE GOAL / Create new goal","UPDATE GOAL / Get created goal", "UPDATE GOAL / Update created goal","UPDATE GOAL / Get updated goal", "UPDATE GOAL / Delete updated goal")
def test_get_goal():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_update = update_goal(goal_id)
    goal_updated_random_name = result_update.json()['goal']["name"]
    assert result_update.status_code == 200
    assert result_update.json()['goal']["name"] == goal_updated_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_updated_random_name
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## UPDATE GOAL NEGATIVE TESTS

@test_steps("UPDATE GOAL / Create new goal", "UPDATE GOAL / Update created goal with invalid goal ID","UPDATE GOAL / Update created goal with invalid token", "UPDATE GOAL / Delete updated goal")
def test_get_goal_negative():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    update_invalid_gid_result = update_goal_invalid_gid()
    assert update_invalid_gid_result.status_code == 401
    assert update_invalid_gid_result.json()['err'] == "Team not authorized"
    assert update_invalid_gid_result.json()['ECODE'] == "OAUTH_027"
    yield

    update_result_invalid_token = update_goal_invalid_token(goal_id)
    assert update_result_invalid_token.status_code == 401
    assert update_result_invalid_token.json()['err'] == "Oauth token not found"
    assert update_result_invalid_token.json()['ECODE'] == "OAUTH_019"
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## DELETE GOAL POSITIVE TESTS

@test_steps("DELETE GOAL / Create new goal","DELETE GOAL / Get created goal", "DELETE GOAL / Delete goal")
def test_get_goal():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

## DELETE GOAL NEGATIVE TESTS

@test_steps("DELETE GOAL / Create new goal","DELETE GOAL / Get created goal", "DELETE GOAL / Delete created goal with invalid goal ID","DELETE GOAL / Delete created goal with invalid token", "DELETE GOAL / Delete goal")
def test_get_goal_negative():

    result_create = create_goal1()
    goal_random_name = result_create.json()['goal']['name']
    goal_id = result_create.json()['goal']['id']
    assert result_create.status_code == 200
    assert result_create.json()['goal']["name"] == goal_random_name
    yield

    get_one_goal_result = get_goal(goal_id)
    assert get_one_goal_result.status_code == 200
    assert get_one_goal_result.json()['goal']["name"] == goal_random_name
    yield

    result_delete_invalid_gid = delete_goal_invalid_gid()
    assert result_delete_invalid_gid.status_code == 500
    assert result_delete_invalid_gid.json()['err'] == "Internal Server Error"
    assert result_delete_invalid_gid.json()['ECODE'] == "22P02"
    yield

    result_delete_invalid_token = delete_goal_invalid_token(goal_id)
    assert result_delete_invalid_token.status_code == 401
    assert result_delete_invalid_token.json()['err'] == "Oauth token not found"
    assert result_delete_invalid_token.json()['ECODE'] == "OAUTH_019"
    yield

    result_delete1 = delete_goal1(goal_id)
    assert result_delete1.status_code == 200
    yield

