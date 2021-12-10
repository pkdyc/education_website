"""
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
"""
from components.security import check_login
import view
import random
import config
from bottle import template

# Initialise our views, all arguments are defaults for the template
page_view = view.View()


# -----------------------------------------------------------------------------
# Index
# -----------------------------------------------------------------------------


def index():
    '''
        index
        Returns the view for the index
    '''
    return page_view("home")


# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

def login_form():
    """
        login_form
        Returns the view for the login_form
    """
    return page_view("login")


def register_form_SQL():
    """
        login_form
        Returns the view for the login_form
    """
    return page_view("register")


def login_form_SQL():
    """
        login_form
        Returns the view for the login_form
    """

    return page_view("loginUserDB")


def login_first():
    """
        request the user to login at first
    """
    return page_view("login_request")


def hacking_response():
    """
        response when detect attacking
    """

    return page_view("hacking")


# -----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    """
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    """

    # By default assume good creds
    login = True

    if username != "admin":  # Wrong Username
        err_str = "Incorrect Username"
        login = False

    if password != "password":  # Wrong password
        err_str = "Incorrect Password"
        login = False

    if login:
        return page_view("valid", name=username)
    else:
        return page_view("invalid", reason=err_str)


def registration_check(username, password):
    """
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    """

    # By default assume good creds
    result = config.registration(username, password)

    if result:
        return True
    else:
        return False


def login_check_sqlite(username, password):
    """
        login_check by using sqlite database
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    """
    login = False

    login = config.login(username, password)

    if login:
        return True
        # return page_view("home", login_status="true")
        # return page_view("valid", name=username)
    else:
        return False
        # return page_view("loginUserDB", login_status="false")
        # return page_view("invalid", reason="incorrect password or username")


# -----------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------

def about():
    '''
        about
        Returns the view for the about page
    '''
    return page_view("about", garble=about_garble())


# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
              "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
              "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
              "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
              "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
              "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]


# -----------------------------------------------------------------------------
# Debug
# -----------------------------------------------------------------------------

def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


# -----------------------------------------------------------------------------
# 404
# Custom 404 error page
# -----------------------------------------------------------------------------

def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body
    error_msg = error_msg.replace("<", "&lt;").replace(">", "&gt;")
    return page_view("error", error_type=error_type, error_msg=error_msg)


# -----------------------------------------------------------------------------
# Tutorial Pages
# -----------------------------------------------------------------------------
def introduction():
    return page_view("introduction")


def frontend_sub1():
    return page_view("frontend_1")


def frontend_sub2():
    return page_view("frontend_2")


def frontend_sub2_1():
    return page_view("frontend_2_1")


def frontend_sub2_2():
    return page_view("frontend_2_2")


def frontend_sub3():
    return page_view("frontend_3")


def frontend_sub3_1():
    return page_view("frontend_3_1")


def frontend_sub4():
    return page_view("frontend_4")


def frontend_sub4_1():
    return page_view("frontend_4_1")


def frontend_sub4_2():
    return page_view("frontend_4_2")


def backend_sub1():
    return page_view("backend_1")


def backend_sub1_1():
    return page_view("backend_1_1")


def backend_sub1_2():
    return page_view("backend_1_2")


def backend_sub2():
    return page_view("backend_2")


def backend_sub2_1():
    return page_view("backend_2_1")


def backend_sub2_2():
    return page_view("backend_2_2")


def backend_sub2_3():
    return page_view("backend_2_3")


def backend_sub2_4():
    return page_view("backend_2_4")


def backend_sub2_5():
    return page_view("backend_2_5")


def backend_sub3():
    return page_view("backend_3")


def backend_sub3_1():
    return page_view("backend_3_1")


def backend_sub3_2():
    return page_view("backend_3_2")


def backend_sub4():
    return page_view("backend_4")


def summary():
    return page_view("summary")


def introduction_sub1():
    return page_view("introduction_1")


def introduction_sub2():
    return page_view("introduction_2")


def introduction_sub3():
    return page_view("introduction_3")

# ADMIN
def admin():
    return page_view("admin")