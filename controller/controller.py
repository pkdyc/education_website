'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''

from bottle import route, get, post, error, request, static_file, response, template
import model
import config
from components.security import check_login
from components.database import get_all_users, delete_user, mute, unmute
import view
import os
import run

page_view = view.View()


def check_waf(path, arg):
    arg = arg.replace('/', "%2F").replace('+', "%2B").replace('?', "%3f").replace('%', "%23").replace('%', "%26")
    arg = arg.replace('=', "%3D").replace(' ', "%20")
    path = "http://{}:{}".format(run.host_a,run.port_a) + path + '/' + arg
    print(path)
    res = os.popen("curl {}".format(path))
    res = res.read()
    return res


# -----------------------------------------------------------------------------
# Static file paths
# -----------------------------------------------------------------------------

# Allow image loading

@route('/img/<picture:path>')
@route('/frontend/img/<picture:path>')
@route('/frontend/css/img/<picture:path>')
@route('/frontend/html/img/<picture:path>')
@route('/frontend/js/img/<picture:path>')
@route('/introduction/img/<picture:path>')
@route('/introduction/css/img/<picture:path>')
@route('/introduction/html/img/<picture:path>')
@route('/introduction/js/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='static/img/')


# -----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
@route('/frontend/css/<css:path>')
@route('/frontend/css/css/<css:path>')
@route('/frontend/html/css/<css:path>')
@route('/frontend/js/css/<css:path>')
@route('/introduction/css/<css:path>')
@route('/introduction/css/css/<css:path>')
@route('/introduction/html/css/<css:path>')
@route('/introduction/js/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='static/css/')


# -----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
@route('/frontend/js/<js:path>')
@route('/frontend/html/js/<js:path>')
@route('/frontend/css/js/<js:path>')
@route('/frontend/js/js/<js:path>')
@route('/introduction/js/<js:path>')
@route('/introduction/html/js/<js:path>')
@route('/introduction/css/js/<js:path>')
@route('/introduction/js/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='static/js/')


# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------

# Redirect to login
@route('/')
@route('/home')
def get_index():
    '''
        get_index
        
        Serves the index page
    '''

    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.index()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


# logout
@post('/home')
def get_index():
    '''
        get_index

        Serves the index page
    '''
    response.set_cookie("loginStatus", "")
    page = model.index()
    return template(page, login_status="false", user_type='none')


@post('/homeChat')
def backToMainFromChat():
    page_token = security_check("chatroom","chatroom")
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()
    page = page_view("home")
    return template(page, login_status="true", register_status="none", user_type='none')


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


# -----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    '''
        get_login
        
        Serves the login page
    '''
    return model.login_form()


@get('/loginSQL')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    page = model.login_form_SQL()
    return template(page, register_status="none", login_status='false', login_attempt="none", user_type='none')


@get('/hacking')
def response_hacking():
    return model.hacking_response()


@get('/registerSQL')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    page = model.register_form_SQL()
    return template(page, register_status="none", login_status='false', user_type='none')


@post('/registerSQL')
def get_register():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    waf_status = check_waf('/waf/account/registration/username', username)
    if waf_status != 'True':
        page = page_view("register")
        return template(page, register_status=waf_status, login_status='false', user_type='none')

    waf_status = check_waf('/waf/account/registration/password', password)
    if waf_status != 'True':
        page = page_view("register")
        return template(page, register_status=waf_status, login_status='false', user_type='none')
    # Call the appropriate method
    reg_stat = model.registration_check(username, password)
    if reg_stat:
        page = page_view("register")
        return template(page, register_status="success", login_status='false', user_type='none')
    else:
        page = page_view("register")
        return template(page, register_status="failed", login_status='false', user_type='none')


# -----------------------------------------------------------------------------

@post('/loginSQL')
def post_login_sql():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    waf_status = check_waf('/waf/account/login', username) == 'True' and check_waf('/waf/account/login',
                                                                                   password) == 'True'
    if not waf_status:
        page = page_view("loginUserDB")
        return template(page, login_status="false", register_status="none", login_attempt="invalid_syntax",
                        user_type='none')

    token = config.getToken_user(username, password)
    response.set_cookie("loginStatus", token)

    # Call the appropriate method
    login_stat = model.login_check_sqlite(username, password)
    if login_stat and username == 'root':
        page = page_view("home")
        return template(page, login_status="true", register_status="none", user_type='admin')
    elif login_stat:
        page = page_view("home")
        return template(page, login_status="true", register_status="none", user_type='user')
    else:
        page = page_view("loginUserDB")
        return template(page, login_status="false", register_status="none", login_attempt="failed", user_type='none')


# -----------------------------------------------------------------------------

@get('/about')
def get_about():
    '''
        get_about
        
        Serves the about page
    '''
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.about()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


# -----------------------------------------------------------------------------

# Help with debugging
@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)


# -----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
@error(404)
def error(error):
    return model.handle_errors(error)


# -----------------------------------------------------------------------------
# Tutorial Pages
# -----------------------------------------------------------------------------

@get('/introduction')
def get_introduction():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.introduction()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/backend')
def get_backend():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/introduction/intro')
def get_introduction_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.introduction_sub1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get("/introduction/tool")
def get_introduction_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.introduction_sub2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get("/introduction/process")
def get_introduction_3():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.introduction_sub3()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/intro')
def get_frontend_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/html')
def get_frontend_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/html/element')
def get_frontend_2_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub2_1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/html/structure')
def get_frontend_2_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub2_2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/css')
def get_frontend_3():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub3()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/css/syntax')
def get_frontend_3():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub3_1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/js')
def get_frontend_4():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub4()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/js/guideline')
def get_frontend_4_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub4_1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/frontend/js/extension')
def get_frontend_4_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.frontend_sub4_2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


@get('/summary')
def get_summary():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.summary()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')


# Admin controller

@get('/admin')
def get_admin():
    user_token = token_check("admin")
    if user_token:
        user_id = user_token[1]
        page = model.admin()
        user_list = get_all_users()
        status = True
        if status and user_id == 'root':
            page = template(page, users=user_list, login_status="true", user_type="admin")
            page = page.replace("(pageToken)", user_token[0])
            return page
        elif status:
            return template(page, users=None, login_status="true", user_type="user")
        else:
            return template(page, users=None, login_status="false", user_type="user")
    else:
        return model.login_first()
    # user_id = config.database.getUserFromToken(token)
    # status = check_login(user_id, token)
    # page = model.admin()
    # user_list = get_all_users()
    # if status and user_id == 'root':
    #     return template(page, users=user_list, login_status="true", user_type="admin")
    # elif status:
    #     return template(page, users=None, login_status="true", user_type="user")
    # else:
    #     return template(page, users=None, login_status="false", user_type="user")


@post('/deleteuser')
def del_user():
    page_token = security_check("admin", "admin")
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    username = request.forms.get('target-user')

    user_id = page_token[1]
    page = model.admin()
    user_list = get_all_users()

    if user_id == 'root':
        delete_user(username)
        user_list = get_all_users()
        return template(page, users=user_list, login_status="true", user_type="admin").replace("(pageToken)", page_token[0])
    else:
        return template(page, users=None, login_status="false", user_type="user")


@post('/muteuser')
def mute_user():
    page_token = security_check("admin", "admin")
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    username = request.forms.get('target-user')

    user_id = page_token[1]
    page = model.admin()
    user_list = get_all_users()

    if user_id == 'root':
        mute(user_id, username)
        return template(page, users=user_list, login_status="true", user_type="admin").replace("(pageToken)", page_token[0])
    else:
        return template(page, users=None, login_status="false", user_type="user")


@post('/unmuteuser')
def unmute_user():
    page_token = security_check("admin", "admin")
    if page_token == "hacking":
        return model.hacking_response()
    if page_token == "logout":
        return model.login_first()

    username = request.forms.get('target-user')

    user_id = page_token[1]
    page = model.admin()
    user_list = get_all_users()

    if user_id == 'root':
        unmute(user_id, username)
        page = template(page, users=user_list, login_status="true", user_type="admin")
        page = page.replace("(pageToken)", page_token[0])
        return page
    else:
        return template(page, users=None, login_status="false", user_type="user")


def token_check(origin_path):
    user_token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(user_token)
    if user_id:
        page_token = config.security.getPage_token(user_token, origin_path)
        return [page_token, user_id]
    else:
        return None


def security_check(origin_path, final_path):
    user_token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(user_token)

    if user_id:
        page_token = request.forms.get("page_token")
        result = config.security.verify_page_token(user_token, origin_path, page_token)
        if result:
            page_token = config.security.getPage_token(user_token, final_path)
            return [page_token, user_id]
        else:
            response.set_cookie("loginStatus", "")
            return "hacking"
    return "logout"
