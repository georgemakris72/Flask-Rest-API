from werkzeug.security import safe_str_cmp  #really only necessary for python 2 to compare strings.  Python 2 somethimes had trouble with something like string1==string2
from user import User  #so now instead of using dictionary like in commented out code below we can use the User class.


users=[User(1,'bob','asdf')]

# users=[
# {
# 'id':1,
# 'username':'bob',
# 'password':'1234'
# }
# ]

username_mapping={u.username: u for u in users}


# username_mapping={'bob':{
# 'id':1,
# 'username':'bob',
# 'password':'1234'
# }}

userid_mapping={u.id: u for u in users}


# userid_mapping={1:{
# 'id':1,
# 'username':'bob',
# 'password':'1234'
# }}

def authenticate(username,password):
    user =User.find_by_username(username)
    if user and user.password==password:
        return user

def identity(payload):#payload unique to flask jwt library
    user_id=payload['identity']
    return User.find_by_id(user_id)

#
