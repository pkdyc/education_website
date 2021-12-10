from bottle import run, request, post, get
import re
import string

# Debug mode to check whether or not attacks are working
# Start with it as "True", try the attack, flip it to false, try the attack again and see if your WAF blocked it
# Debug should be set to false when launching the final version
debug = False


def sql_inject_detect(password):
    pattern = '[\.\+;?\\\\\( +)(=)(/)%]'
    result = re.search(pattern, password)
    return result is not None


@post('/waf/detect/<string_in:path>')
def detect_attack(string_in):
    if not debug:
        if 'attack' in string_in:
            return 'False'
        return 'True'
    return 'False'


@post('/waf/email/<email:path>')
def verify_email(email):
    if '@' in email:
        return 'True'
    else:
        return "Not an email address"


@get('/waf/account/registration/password/<password>')
def verify_password(password):
    if sql_inject_detect(password):
        return "failed : contain invalid character [.\\+?-;=/]"
    if len(password) < 6 and len(password) < 16:
        return "length of password must in the range of 6 to 16"

    if not any(c in string.ascii_lowercase for c in password):
        return "Password must contain at least one lowercase character"

    if not any(c in string.ascii_uppercase for c in password):
        return "Password must contain at least one uppercase character"

    return 'True'


@get('/waf/account/registration/username/<password>')
def verify_password(password):
    if sql_inject_detect(password):
        return "failed : contain invalid character [.\\+?-;=/]"
    if not len(password) >= 5 and len(password) < 16:
        return "length of username must in the range of 5 to 16"
    return 'True'


@get('/waf/account/login/<password>')
def match_login(password):
    if sql_inject_detect(password):
        return "failed : contain invalid character [.\\+?-;=/]"
    return 'True'


# Rather than using paths, you could throw all the requests with form data filled using the
# requests module and extract it here. Alternatively you could use JSON objects.

# Custom definition waf
@post('/waf/custom/field=<field:path>%20test=<test:path>')
def custom_waf(field, test):
    if re.search(test, field) is not None:
        return "True"
    return "False"


# Debug toggle
@post('/waf/debug')
def enable_debugger():
    global debug
    if debug:
        debug = False
    else:
        debug = True
    return str(debug)


# Run the server
def waf_start(host, port):
    run(host=host, port=port)
