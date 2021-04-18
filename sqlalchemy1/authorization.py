from models.usercreation import usermodel

def authenticate(username,password):
    user=usermodel.usernamemapping(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return usermodel.useridmapping(user_id)