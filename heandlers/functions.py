import json

def check_user_group(kourse:str, group:str):
    with open(file='data/json/groups_key.json', mode='r') as f:
        data = json.load(f)
    try :
        data['bakalavr'][kourse][group]
        return True
    except :
        return False
# check_user_group(kourse='1', group='Б743')