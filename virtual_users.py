import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass
import random

from selenium import webdriver

#------------------------------------------------

default_target = "https://10.86.228.68/"

#------------------------------------------------
# Usage: 
# python3 virtual_users.py
#------------------------------------------------

#------------------------------------------------
# Virtual_user 1: 
# Register with random username and Login
#------------------------------------------------
def virtual_user1(target):
    driver = webdriver.Firefox()
    driver.get(target)

    # Hit the Register button
    reg_button = driver.find_element_by_id("register")
    reg_button.click()

    print("Register")

    username = "test" + str(random.randint(20,1000))
    password = "Aa000000"

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    register_btn = driver.find_element_by_id("register-submit")
    register_btn.click()

    time.sleep(3)

    # Hit the Login button
    login_button = driver.find_element_by_id("login")
    login_button.click()

    time.sleep(1)

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()

    print("Logged in!")

    time.sleep(2)

    print("Testing finished, closing web driver.")
    driver.close()

#------------------------------------------------
# Virtual_user 2: 
# Register with existing username and login with wrong password
#------------------------------------------------
def virtual_user2(target):
    driver = webdriver.Firefox()
    driver.get(target)

    username = "test11"
    password = "Aa000000"

    # Hit the Register button
    reg_button = driver.find_element_by_id("register")
    reg_button.click()

    print("Register with test11 (exist)")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    register_btn = driver.find_element_by_id("register-submit")
    register_btn.click()

    time.sleep(3)

    # Hit the Login button
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    print("Login with test11 (exist)")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()

    time.sleep(2)

    print("Testing finished, closing web driver.")
    driver.close()

#------------------------------------------------
# Virtual_user 3: 
# Walk through tutorial contents without login
#------------------------------------------------
def virtual_user3(target):
    driver = webdriver.Firefox()
    driver.get(target)

    time.sleep(2)

    # Walk through tutorial pages
    main_group_xpath = '/html/body/div[@class="home"]/div[@class="main-nav"]/div[@class="btn"]'

    for index in range(4):
        container = driver.find_elements_by_xpath(main_group_xpath)
        container[index].click()
        time.sleep(3)

        if (index == 3):
            time.sleep(3)
            break

        tutorial_xpath = '/html/body/div[@class="tutorial-container"]/div[@class="nav-div"]/ul[@class="nav-list"]/li[@class="nav-li"]'
        side_nav_container = driver.find_elements_by_xpath(tutorial_xpath)
        size = len(side_nav_container)

        for j in range(size):
            s_container = driver.find_elements_by_xpath(tutorial_xpath)
            s_container[j].click()
            time.sleep(3)

        home_btn = driver.find_element_by_id("home")
        home_btn.click()
        time.sleep(3)
    
    print("Testing finished, closing web driver.")
    driver.close()

#------------------------------------------------
# Virtual_user 4: 
# Create new post in discussion form
# Reply to other posts in discussion form
#------------------------------------------------
def virtual_user4(target):
    driver = webdriver.Firefox()
    driver.get(target)
    print("Login")
    username = "root"
    password = "admin123"

    # Hit the Login button
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()

    time.sleep(2)

    # Walk through discussion form

    discussion_btn = driver.find_element_by_id("discussion-entry")
    discussion_btn.click()
    time.sleep(1)

    discussion_item_xpath = '//*[@id="discussion_form"]/div/div[2]'
    discussion_item = driver.find_element_by_xpath(discussion_item_xpath)
    discussion_item.click()
    time.sleep(1)

    print("Replying to this post")

    reply_field = driver.find_element_by_name("reply_msg")
    reply_field.send_keys("Aha My Reply Test")
    time.sleep(1)

    reply_btn_xpath = '//*[@id="put_reply"]/a'
    reply_btn = driver.find_element_by_xpath(reply_btn_xpath)
    reply_btn.click()
    time.sleep(2)

    create_post_xpath = '/html/body/div/div[1]/div[1]/div[1]'
    create_post_btn = driver.find_element_by_xpath(create_post_xpath)
    create_post_btn.click()
    time.sleep(1)

    print("Creating new post")

    post_title_field = driver.find_element_by_name("reply_msg")
    post_title_field.send_keys("Aha My New Post")
    time.sleep(1)

    reply_btn_xpath = '//*[@id="put_reply"]/a'
    reply_btn = driver.find_element_by_xpath(reply_btn_xpath)
    reply_btn.click()
    time.sleep(2)

    # Hit the Leave button
    leave_xpath = '/html/body/div/div[1]/div[1]/div[2]/form/input'
    leave_button = driver.find_element_by_xpath(leave_xpath)
    leave_button.click()
    time.sleep(1)

    # Hit the Logout button
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(1)

    print("Testing finished, closing web driver.")
    driver.close()


#------------------------------------------------
# Virtual_user 5: 
# Admin user: Mute, Unmute, Delete users
#------------------------------------------------
def virtual_user5(target):
    driver = webdriver.Firefox()
    driver.get(target)
    # Create a temporary user for testing
    # Hit the Register button
    reg_button = driver.find_element_by_id("register")
    reg_button.click()

    print("Register")

    username = "test" + str(random.randint(20,1000))
    password = "Aa000000"

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    time.sleep(1)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    register_btn = driver.find_element_by_id("register-submit")
    register_btn.click()

    time.sleep(3)

    # Hit the Login button to login as ADMIN
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    admin_username = 'root'
    admin_password = 'admin123'

    print("Login as admin")

    # Enter admin username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(admin_username)
    time.sleep(1)

    # Enter admin password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(admin_password)
    time.sleep(1)

    # Hit the submit button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()
    time.sleep(1)

    # Demo admin control
    admin_btn_xpath = '/html/body/ul/li[4]/a'
    admin_btn = driver.find_element_by_xpath(admin_btn_xpath)
    admin_btn.click()

    print("Entering admin control page")

    # Mute
    mute_target_child_xpath = '//*[text()="{}"]'.format(username)
    mute_target_child = driver.find_element_by_xpath(mute_target_child_xpath)
    mute_btn_xpath = '../../div[3]/form/button'
    mute_btn = mute_target_child.find_element_by_xpath(mute_btn_xpath)
    mute_btn.click()

    print("{} has been muted", username)

    time.sleep(1)

    admin_helper1(target, username, password)

    time.sleep(8)

    # Unmute
    unmute_target_child = driver.find_element_by_xpath(mute_target_child_xpath)
    unmute_btn_xpath = '../../div[2]/form/button'
    unmute_btn = unmute_target_child.find_element_by_xpath(unmute_btn_xpath)
    unmute_btn.click()

    print("{} has been unmuted", username)

    time.sleep(1)

    admin_helper2(target, username, password)

    time.sleep(13)

    # Delete
    delete_target_child = driver.find_element_by_xpath(mute_target_child_xpath)
    delete_btn_xpath = '../../div[4]/form/button'
    delete_btn = delete_target_child.find_element_by_xpath(delete_btn_xpath)
    delete_btn.click()

    print("{} has been deleted", username)

    time.sleep(1)

    admin_helper3(target, username, password)

    time.sleep(8)

    print("Testing finished, closing web driver.")
    driver.close()

#------------------------------------------------
# Admin test helper 1: 
# Admin user: Test if the user has been muted
#------------------------------------------------
def admin_helper1(target, username, password):
    driver = webdriver.Firefox()
    driver.get(target)

    # Hit the Login button to login with given user
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    print("Login")

    # Enter admin username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)

    # Enter admin password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)

    # Hit the submit button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()
    time.sleep(1)

    # Enter discussion form to see if user can reply
    discussion_btn = driver.find_element_by_id("discussion-entry")
    discussion_btn.click()
    time.sleep(1)

    discussion_item_xpath = '//*[@id="discussion_form"]/div/div[2]'
    discussion_item = driver.find_element_by_xpath(discussion_item_xpath)
    discussion_item.click()
    time.sleep(3)

    driver.close()

#------------------------------------------------
# Admin test helper 2: 
# Admin user: Test if the user has been unmuted
#------------------------------------------------
def admin_helper2(target, username, password):
    driver = webdriver.Firefox()
    driver.get(target)

    # Hit the Login button to login with given user
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    print("Login")

    # Enter admin username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)

    # Enter admin password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)

    # Hit the submit button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()
    time.sleep(1)

    # Enter discussion form to see if user can reply
    discussion_btn = driver.find_element_by_id("discussion-entry")
    discussion_btn.click()
    time.sleep(1)

    discussion_item_xpath = '//*[@id="discussion_form"]/div/div[2]'
    discussion_item = driver.find_element_by_xpath(discussion_item_xpath)
    discussion_item.click()
    time.sleep(1)

    print("Replying to this post")

    reply_field = driver.find_element_by_name("reply_msg")
    reply_field.send_keys("Aha I can talk again!")
    time.sleep(2)

    reply_btn_xpath = '//*[@id="put_reply"]/a'
    reply_btn = driver.find_element_by_xpath(reply_btn_xpath)
    reply_btn.click()
    time.sleep(1)

    driver.close()

#------------------------------------------------
# Admin test helper 3: 
# Admin user: Test if the user has been deleted
#------------------------------------------------
def admin_helper3(target, username, password):
    driver = webdriver.Firefox()
    driver.get(target)

    # Hit the Login button to login with given user
    login_button = driver.find_element_by_id("login")
    login_button.click()
    time.sleep(1)

    print("Login")

    # Enter admin username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)

    # Enter admin password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)

    # Hit the submit button
    login_btn = driver.find_element_by_id("login-submit")
    login_btn.click()
    time.sleep(2)

    driver.close()


#------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

    user = random.randint(1, 5)
    print("Executing virtual user", user)
    
    if (user == 1):
        virtual_user1(target_url)
    elif (user == 2):
        virtual_user2(target_url)
    elif (user == 3):
        virtual_user3(target_url)
    elif (user == 4):
        virtual_user4(target_url)
    elif (user == 5):
        virtual_user5(target_url)
    
print("Finished!")
