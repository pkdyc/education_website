'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''

from components.database import login
from bottle import route, get, post, error, request, static_file, response, template
import model
import config
from components.security import check_login
import view
page_view = view.View()

# -----------------------------------------------------------------------------
# Static file paths
# -----------------------------------------------------------------------------

# Allow image loading

@route('/img/<picture:path>')
@route('/backend/img/<picture:path>')
@route('/backend/sql/img/<picture:path>')
@route('/backend/intro/img/<picture:path>')
@route('/backend/bottle/img/<picture:path>')
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
@route('/backend/css/<css:path>')
@route('/backend/sql/css/<css:path>')
@route('/backend/intro/css/<css:path>')
@route('/backend/bottle/css/<css:path>')
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
@route('/backend/js/<js:path>')
@route('/backend/intro/js/<js:path>')
@route('/backend/sql/js/<js:path>')
@route('/backend/bottle/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='static/js/')


@get('/backend/intro')
def get_backend_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/intro/info')
def get_backend_1_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub1_1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')
    
@get('/backend/intro/restapi')
def get_backend_1_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub1_2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql')
def get_backend_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql/connect')
def get_backend_2_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2_1()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql/table')
def get_backend_2_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2_2()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql/insert')
def get_backend_2_3():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2_3()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql/query')
def get_backend_2_4():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2_4()
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/sql/delete')
def get_backend_2_5():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub2_5()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/bottle')
def get_backend_3():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub3()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/bottle/route')
def get_backend_3_1():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub3_1()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')

@get('/backend/bottle/gp')
def get_backend_3_2():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub3_2()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')
    
@get('/backend/end')
def get_backend_4():
    token = request.get_cookie("loginStatus")
    user_id = config.database.getUserFromToken(token)
    status = check_login(user_id, token)
    page = model.backend_sub4()  
    if status and user_id == 'root':
        return template(page, login_status="true", user_type='admin')
    elif status:
        return template(page, login_status="true", user_type='user')
    else:
        return template(page, login_status="false", user_type='none')