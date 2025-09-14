from pathlib import Path
import json
def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """问候用户，并指出其姓名"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"welcome back, {username}!")
    else:
        username = input("what is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"we'll remember you when you come back, {username}!")

greet_user()