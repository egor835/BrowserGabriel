#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()
action = form.getfirst("action", "")

from lib_gpt import Fetch
fetch = Fetch()

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Type !reset</title>
</head>
<body>
    ChatGPT
    <form action="/cgi-bin/chat.py">
        <textarea name="action"></textarea>
        <input type="submit">
    </form>
</body>
</html>
'''


print('Content-type: text/html\n')
print(pattern)
fetch.cre(action)

answer = fetch.read()
print(answer)



#print("<p>Bot: {}</p>".format(response))

