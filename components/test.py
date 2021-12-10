import os
import re

# /waf/password/<password:path>'
# import components.waf as waf
# import threading
#
#
# class Waf_thread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         waf.waf_start()
#
# Waf_thread().start()
# .replace(/\+/g, '%2B').replace(/\"/g,'%22').replace(/\'/g, '%27').replace(/\//g,'%2F')
s = ' curl http://localhost:8081/waf/account/login/pkdyc12％252F1212'
res = os.popen(' curl http://localhost:8081/waf/account/login/pkdyc12％252F1212')
print("result is {}".format(res.read()))
#print(res)
# pattern = '[\.\+;\?\\\\( )\-]'
# pattern = '[\?]'
# string = "121?21&"
# a = re.search(pattern, "1???")
# print(a)