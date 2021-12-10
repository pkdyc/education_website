import datetime

import config

import hmac
import sqlite3
import hashlib
import string
from random import randint, choice


# make sure sqlite3 is installed before running the program

def generateToken(username):
    length = randint(0, 10)
    chars = string.ascii_letters + string.digits
    key = ''.join([choice(chars) for i in range(length)]).encode("utf-8")
    signature = hmac.new(key, username.encode("utf-8"), digestmod=hashlib.sha256)
    return str(signature.hexdigest().encode(), encoding="utf-8")


class UserDB:
    """
    this database which base on sqlite3
    used for login and registration identification
    """

    def __init__(self):
        """
        get the path of userDB, create userDB if not exit, otherwise skips the step of
        initialization
        """
        self.conn = sqlite3.connect("components/userDB.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table if not exists student (                \
                                        name text primary key ,                  \
                                        password text                            \
                                                                );")
        self.conn.commit()

    def check_login(self, cur, username, password):
        cur.execute("select * from student where name = :name", {'name': username})
        res = cur.fetchall()
        if not res:
            return False
        res = res[0][1]
        cur.execute("select * from salts where username = :name", {'name': username})
        salt = cur.fetchall()[0][1]
        obj = hashlib.md5(salt.encode())
        obj.update(password.encode())
        result = obj.hexdigest()
        return result == res

    def login_userDB(self, username, password):
        # return true if there is a such user with entered password
        return self.check_login(self.cursor, username, password)

    def registration_userDB(self, username, password):
        # return false if there is a user with identical name
        try:
            salt = generateToken(username)
            obj = hashlib.md5(salt.encode())
            obj.update(password.encode())
            password = obj.hexdigest()
            self.cursor.execute("insert into salts values (?,?)", (username, salt))
            self.cursor.execute("insert into student values (?,?,?,?);", (username, password, "STANDARD", "FALSE"))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            return False

    def put_Thread(self, owner_id, title):
        # adding new thread to the discussion forum
        try:
            self.cursor.execute("insert into POST (owner_id,title,data) VALUES (?,?,?)",
                                (owner_id, title, str(datetime.datetime.now())))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(e)
            return False

    def construct_DB_for_chat(self):
        try:
            self.cursor.execute("create table if not exists POST("
                                "   post_id integer primary key autoincrement,"
                                "   owner_id text not null ,"
                                "   title text not null ,"
                                "   data text"
                                ");")

            self.cursor.execute("create table if not exists REPLY("
                                "   post_id integer not null,"
                                "   message text not null,"
                                "   sender_id integer not null,"
                                "   reply_id integer primary key autoincrement"
                                "   date  text"
                                ");")

            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            return False

    def reset_all(self):
        # reset all the database and refresh the content inside
        self.cursor.execute("drop table if exists POST;")
        self.cursor.execute("create table if not exists POST("
                            "   post_id integer primary key autoincrement,"
                            "   owner_id text not null ,"
                            "   title text not null ,"
                            "   data text"
                            ");")
        self.cursor.execute("drop table if exists REPLY;")
        self.cursor.execute("create table if not exists REPLY("
                            "   post_id integer not null,"
                            "   message text not null,"
                            "   sender_id integer not null,"
                            "   reply_id integer primary key autoincrement,"
                            "   date  text"
                            ");")
        self.conn.commit()

    def get_all_post(self):
        self.cursor.execute("select * from POST;")
        result = self.cursor.fetchall()
        return result

    def get_one_post(self, post_id):
        self.cursor.execute("select * from POST where post_id = :id;", {'id': post_id})
        result = self.cursor.fetchall()
        return result[0]

    def get_replies(self, post_id):
        self.cursor.execute("select * from REPLY where post_id = :id;", {'id': post_id})
        result = self.cursor.fetchall()
        return result

    def put_reply(self, post_id, msg, sender_id):
        # adding a new reply to a post
        self.cursor.execute("insert into REPLY (post_id,message,sender_id,date) VALUES (?,?,?,?)",
                            (post_id, msg, sender_id, str(datetime.datetime.now())))
        self.conn.commit()

        pass

    def isMuted(self, username):
        self.cursor.execute("select * from student where name = :user_name;", {'user_name': username})
        result = self.cursor.fetchall()[0]
        if result and result[3] == "TRUE":
            return True
        return False

    def muteSomeone(self, adminName, othersName):
        self.cursor.execute("select * from student where name = :user_name;", {'user_name': adminName})
        result = self.cursor.fetchall()
        if result and result[0][2] == "ADMIN":
            self.cursor.execute("select * from student where name = :user_name;", {'user_name': othersName})
            result = self.cursor.fetchall()
            if result and result[0][2] != "ADMIN":
                self.cursor.execute("update student set Muted='TRUE' where name = :user_name;",
                                    {'user_name': othersName})
                self.conn.commit()
                return True
        return False

    def unMuteSomeone(self, adminName, othersName):
        self.cursor.execute("select * from student where name = :user_name;", {'user_name': adminName})
        result = self.cursor.fetchall()
        if result and result[0][2] == "ADMIN":
            self.cursor.execute("select * from student where name = :user_name;", {'user_name': othersName})
            result = self.cursor.fetchall()
            if result and result[0][2] != "ADMIN":
                self.cursor.execute("update student set Muted='FALSE' where name = :user_name;",
                                    {'user_name': othersName})
                self.conn.commit()
                return True
        return False

    def getUserFromToken(self, token):
        a = config.security.allSessionUser
        for k, v in a.items():
            if v.key == token:
                return k
        return None

    def getUserFromUsername(self, username):
        self.cursor.execute("select * from student where name = :user_name;", {'user_name': username})
        result = self.cursor.fetchall()
        return result

    def deleteUser(self, username):
        self.cursor.execute("delete from student where name = '{}';".format(username))
        self.conn.commit()
        return None

    def getAllUsers(self):
        self.cursor.execute("select name from student;")
        result = self.cursor.fetchall()
        return result

    def getNextPost(self):
        self.cursor.execute("select max(post_id) from POST;")
        result = self.cursor.fetchall()
        result = result[0][0]
        return result


# the contents above are the class method, the code below are the python file (package) method
database = UserDB()


def login(username, password):
    return database.login_userDB(username, password)


def registration(username, password):
    return database.registration_userDB(username, password)


def get_all_post():
    return database.get_all_post()

def get_all_users():
    res = database.getAllUsers()
    users = []
    for each in res:
        users.append(each[0])
    return users

def mute(adminName, othersName):
    return database.muteSomeone(adminName, othersName)

def unmute(adminName, othersName):
    return database.unMuteSomeone(adminName, othersName)

def delete_user(username):
    database.deleteUser(username)