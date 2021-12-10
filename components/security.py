import hashlib
import hmac
from hashlib import sha256
import string
from random import choice, randint
from bottle import response
import components.database as database

allSessionUser = {}

allSessionPage = {}


def getUserFromToken(token):
    for k, v in allSessionUser.items():
        if v.key == token:
            return k
    return None


def getPage_token(user_token, cur_page):
    salt = generateToken(cur_page)
    obj = hashlib.md5(salt.encode())
    obj.update(user_token.encode())
    page_token = obj.hexdigest()
    allSessionPage[page_token] = [user_token, cur_page]
    return page_token


def verify_page_token(user_token, cur_page, page_token):
    if page_token in allSessionPage.keys() and [user_token, cur_page] == allSessionPage[page_token]:
        allSessionPage.pop(page_token)
        return True
    else:
        return False


def getToken_user(username, password):
    if database.login(username, password) and username in allSessionUser.keys():
        return allSessionUser[username].key
    elif database.login(username, password) and username not in allSessionUser.keys():
        allSessionUser[username] = Session(username)
        return allSessionUser[username].key
    else:
        return "failed"


def generateToken(username):
    length = randint(0, 10)
    chars = string.ascii_letters + string.digits
    key = ''.join([choice(chars) for i in range(length)]).encode("utf-8")
    signature = hmac.new(key, username.encode("utf-8"), digestmod=sha256)
    return str(signature.hexdigest().encode(), encoding="utf-8")


def verifyToken_user(username, token):
    return username in allSessionUser.keys() and allSessionUser[username].key == token


class Session:
    def __init__(self, username):
        self.key = generateToken(username)


def check_login(username, token):
    return username in allSessionUser.keys() and allSessionUser[username].key == token


def get_currentLoginByToken(token):
    return database.database.getUserFromToken(token)
