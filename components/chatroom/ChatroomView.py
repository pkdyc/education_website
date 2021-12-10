from bottle import request, response

import config
import sys
import os


def mutedPage(page, username):
    if config.database.isMuted(username):
        page = page.replace(
            '<input onclick="location.href=\'/chatroom\';" value="post" style="text-align: left" />', '')
        page = page.replace('<a class="button" onclick="c(\'text_area\')">post</a>', '')
    return page


class ChatroomView:
    def __init__(self):

        template_file = open(r"templates/chatroom/chat_post_template.html")
        self.post_template = "".join(template_file.readlines())
        template_file.close()

        template_file = open("templates/chatroom/chat_reply_template.html")
        self.reply_template = "".join(template_file.readlines())
        template_file.close()

        template_file = open("templates/chatroom/chat_template.html")
        self.main_page = "".join(template_file.readlines())
        template_file.close()

    def getPage_main(self, userid):
        thread_location = r'("the place to put in thread list")'
        page = self.main_page.replace(r'("thread title")', "post new thread")
        page = page.replace(thread_location, self.inner_thread())

        replies_location = r'("the place to put in chatting list")'
        page = page.replace(replies_location, "")
        page = page.replace(r'action="/chatroom_reply"', r'action="/chatroom_post"')

        return mutedPage(page, userid)

    def getPage_main_demo(self, userid, page_token):
        thread_location = r'("the place to put in thread list")'
        page = self.main_page.replace(r'("thread title")', "post new thread")
        page = page.replace(thread_location, self.inner_thread())

        replies_location = r'("the place to put in chatting list")'
        page = page.replace(replies_location, "")
        page = page.replace(r'action="/chatroom_reply"', r'action="/chatroom_post"')

        page = page.replace("(pageToken)", page_token)  # set page token

        return mutedPage(page, userid)

    def getPage_withReplies(self, post_id, username, page_token):
        title = config.database.get_one_post(post_id)[2].replace("<", "&lt;").replace(">", "&gt;")
        thread_location = r'("the place to put in thread list")'
        page = self.main_page.replace(thread_location, self.inner_thread())
        page = page.replace(r'("thread title")', title)
        replies_location = r'("the place to put in chatting list")'
        page = page.replace(replies_location, self.inner_reply(post_id, username))

        page = page.replace("(pageToken)", page_token)  # set page token
        return mutedPage(page, username)

    def inner_thread(self):
        middle = ""
        all_post = config.get_all_post()
        for post in all_post:
            title = post[2].replace("<", "&lt;").replace(">", "&gt;")
            middle += self.post_template.replace("title-content", title) \
                .replace("sender-content", post[1]).replace("(the post id)", str(post[0])) \
                .replace("_form", "_form" + str(post[0]))

        return middle

    def inner_reply(self, post_id, username):
        res = ""
        for reply in config.database.get_replies(post_id):
            content = reply[1].replace("<", "&lt;").replace(">", "&gt;")
            if reply[2] == username:
                temp = self.reply_template.replace("(profile_path)", "img/self_profile.png")

                temp = temp.replace("replier-content", reply[2]).replace("reply-content", content)
            else:
                temp = self.reply_template.replace("(profile_path)", "img/others_profile.png").replace(
                    "<li class=\"self\">", "<li class=\"other\">")
                temp = temp.replace("replier-content", reply[2]).replace("reply-content", content)
            time = str(reply[4]).split(".")[0]
            temp = temp.replace('"(the time)"', time)
            res += temp
        return res


