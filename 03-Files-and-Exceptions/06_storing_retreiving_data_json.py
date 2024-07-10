# * Using JSON for storing data:

# *** Using json.dumps() and json.loads():

# from pathlib import Path
# import json

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# contents = json.dumps(nums)

# path = Path('json/numbers.json')
# path.write_text(contents)


# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)

# *** Saving and restoring User-Generated Data:

# from pathlib import Path
# import json

# path = Path('json/username.json')

# if path.exists():
#     username = path.read_text()
#     username = json.loads(username)
#     print(f"Welcome Back, {username}")

# else:
#     username = input("Hello, Please input your username: ")
#     json_username = json.dumps(username)
#     path.write_text(json_username)


# ** Refactoring above code for Saving and restoring User-Generated Data: 

from pathlib import Path
import json

def greet_user():
    path = Path('json/username.json')
    
    username = get_stored_username(path)
    if username:
        print(f"Welcome Back, {username}")
        
    else:
        get_new_username(path)


def get_stored_username(path):
    if path.exists():
        username = path.read_text()
        return json.loads(username)
    else:
        return None

def get_new_username(path):
    username = input("Hello, Please input your username: ")
    json_username = json.dumps(username)
    path.write_text(json_username)


greet_user()