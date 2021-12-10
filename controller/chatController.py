from bottle import route, get, post, error, request, static_file, response, template
import bottle
import model
from components.chatroom.ChatroomView import *

room = ChatroomView()
page = model.index()


def token_check():
    user_token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(user_token)
    if user_id:
        page_token = config.security.getPage_token(user_token, "chatroom")
        return [page_token, user_id]
    else:
        return None


def security_check():
    user_token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(user_token)

    if user_id:
        page_token = request.forms.get("page_token")
        result = config.security.verify_page_token(user_token, "chatroom", page_token)
        if result:
            page_token = config.security.getPage_token(user_token, "chatroom")
            return [page_token, user_id]
        else:
            response.set_cookie("loginStatus", "")
            return "hacking"
    return "logout"


@route("/testing")
def enter_message():
    return "qwq"


@route("/chatroom")
def get_chatroom():
    # check user token
    page_token = token_check()

    if page_token is None:
        return model.login_first()

    return room.getPage_main_demo(page_token[1], page_token[0])


@post("/chatroomThread")
def get_chatroom():
    page_token = security_check()
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    post_id = request.query.page
    response.set_cookie("current_post", post_id)
    return room.getPage_withReplies(post_id, page_token[1], page_token[0])


@post("/chatroom_reply")
def put_reply():
    page_token = security_check()
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    post_id = request.get_cookie("current_post")
    msg = request.forms.get("reply_msg")
    config.database.put_reply(post_id, msg, page_token[1])
    return room.getPage_withReplies(post_id, page_token[1], page_token[0])


@post('/chatroom_post')
def put_discussion():
    page_token = security_check()
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    post_id = config.database.getNextPost()
    msg = request.forms.get("reply_msg")
    config.database.put_Thread(page_token[1], msg)
    return room.getPage_withReplies(post_id, page_token[1], page_token[0])
