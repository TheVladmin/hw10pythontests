import requests
from faker import Faker
fake = Faker()
from dotenv import load_dotenv
import os
load_dotenv()

request_headers = {"Authorization":os.getenv("token"), 'Content-Type': 'application/json'}
team_id = os.getenv("team_id")

# Створення першого goal
def create_goal1():
    goal_random_name = fake.first_name()
    body = {
        "name": goal_random_name
    }
    result_create = requests.post(f"https://api.clickup.com/api/v2/team/{team_id}/goal", headers=request_headers, json=body)
    return result_create

# Створення другого goal
def create_goal2():
    goal_random_name2 = fake.first_name()
    body = {
        "name": goal_random_name2
    }
    result_create2 = requests.post(f"https://api.clickup.com/api/v2/team/{team_id}/goal", headers=request_headers, json=body)
    return result_create2

# Отримання усіх goals
def get_goals():
    result_get_goals = requests.get(f"https://api.clickup.com/api/v2/team/{team_id}/goal", headers=request_headers)
    return result_get_goals


# Видалення першого goal
def delete_goal1(goal_id):
    result_delete1 = requests.delete("https://api.clickup.com/api/v2/goal/" + str(goal_id), headers=request_headers)
    return result_delete1

# Видалення другого goal
def delete_goal2(goal2_id):
    result_delete2 = requests.delete("https://api.clickup.com/api/v2/goal/" + str(goal2_id), headers=request_headers)
    return result_delete2


# Отримання одного goal
def get_goal(goal_id):
    get_one_goal_result = requests.get("https://api.clickup.com/api/v2/goal/" + str(goal_id), headers=request_headers)
    return get_one_goal_result

# Оновлення goal
def update_goal(goal_id):
    goal_updated_random_name = fake.first_name()
    body_update = {
        "name": goal_updated_random_name
    }
    result_update = requests.put("https://api.clickup.com/api/v2/goal/" + str(goal_id), headers=request_headers,json=body_update)
    return result_update



#НЕГАТИВНІ ТЕСТИ

# Отримання усіх goals with invalid team ID

def get_goals_invalid_team_id():
    result_get_goals_invalid_fid = requests.get(f"https://api.clickup.com/api/v2/team/123/goal", headers=request_headers)
    return result_get_goals_invalid_fid

# Отримання усіх goals with invalid token

def get_goals_invalid_token():
    result_get_goals_invalid_token = requests.get(f"https://api.clickup.com/api/v2/team/{team_id}/goal", headers= {'Authorization': '123'})
    return result_get_goals_invalid_token

# Створення одного goal with invalid team ID
def create_goal_invalid_tid():
    goal_random_name = fake.first_name()
    body = {
        "name": goal_random_name
    }
    result_create_invalid_tid = requests.post(f"https://api.clickup.com/api/v2/team/123/goal", headers=request_headers, json=body)
    return result_create_invalid_tid

# Створення одного goal with invalid token
def create_goal_invalid_token():
    goal_random_name = fake.first_name()
    body = {
        "name": goal_random_name
    }
    result_create_invalid_token = requests.post(f"https://api.clickup.com/api/v2/team/{team_id}/goal", headers= {'Authorization': '123'}, json=body)
    return result_create_invalid_token

# Отримання одного goal with invalid goal ID
def get_goal_invalid_lid():
    get_one_goal_invalid_gid_result = requests.get("https://api.clickup.com/api/v2/goal/" + '123', headers=request_headers)
    return get_one_goal_invalid_gid_result

# Отримання одного goal with invalid token
def get_goal_invalid_token(goal_id):
    get_one_goal_invalid_token_result = requests.get("https://api.clickup.com/api/v2/goal/" + str(goal_id), headers= {'Authorization': '123'})
    return get_one_goal_invalid_token_result


# Оновлення goal with invalid goal ID
def update_goal_invalid_gid():
    goal_updated_random_name = fake.first_name()
    body_update = {
        "name": goal_updated_random_name
    }
    update_invalid_gid_result = requests.put("https://api.clickup.com/api/v2/goal/" + '123', headers=request_headers,json=body_update)
    return update_invalid_gid_result

# Оновлення goal with invalid token
def update_goal_invalid_token(goal_id):
    goal_updated_random_name = fake.first_name()
    body_update = {
        "name": goal_updated_random_name
    }
    update_result_invalid_token = requests.put("https://api.clickup.com/api/v2/goal/" + str(goal_id), headers= {'Authorization': '123'},json=body_update)
    return update_result_invalid_token

# Видалення першого goal with invalid goal ID
def delete_goal_invalid_gid():
    result_delete_invalid_gid = requests.delete("https://api.clickup.com/api/v2/goal/" + '1223', headers=request_headers)
    return result_delete_invalid_gid

# Видалення першого goal with invalid token
def delete_goal_invalid_token(goal_id):
    result_delete_invalid_token = requests.delete("https://api.clickup.com/api/v2/list/" + str(goal_id), headers= {'Authorization': '123'})
    return result_delete_invalid_token