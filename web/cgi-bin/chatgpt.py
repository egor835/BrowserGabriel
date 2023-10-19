#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import os
form = cgi.FieldStorage()
action = form.getfirst("action", "")

from lib_gpt import Fetch
fetch = Fetch()
fetch.cre(action)
answer = fetch.read().replace("\n", "<br>").replace("```python", "Python code:<pre>").replace("```","</pre>")

if os.path.isfile("generating_gpt") == True:
    form1 = '''<div class="fff">
            <img src="/assets/wait_m.gif" class="yopta">
            </div>'''
    meth = '<meta http-equiv="refresh" content="5;url=/cgi-bin/chatgpt.py">'
else:
    form1 = '''<form id="user-input" action="/cgi-bin/chatgpt.py">
            <input type="text" id="action" name="action">
            <button type="submit" id="submit-button">Отправить</button>
            </form>'''
    meth = ''

if action != '':
    meth = '<meta http-equiv="refresh" content="2;url=/cgi-bin/chatgpt.py">'

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>OpenAI</title>
''' + meth + '''
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f8fa;
        margin: 0;
        padding: 0;
    }

    #header {
        background-color: #000000;
        color: #fff;
        text-align: center;
        padding: 10px;
    }

    .UltraDiv {
        max-width: 800px;
        margin: 20px auto;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 20px;
    }

    #message {
        font-size: 16px;
        margin-bottom: 10px;
    }

    #user-input {
        display: flex;
    }

    #action {
        flex: 1;
        padding: 5px;
    }

    #submit-button {
        background-color: #000000;
        color: #fff;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 3px;
    }

    .img {
        text-align: center;
    }

    .copyright {
        text-align: center;
        color: black;
    }

    .UltraDiv {
    position: relative;
    transition: all 0.5s ease-in-out;
  }

  .UltraDiv:hover {
    transform: translateY(-10px);
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
  }

  .UltraDiv {
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    transition: all 0.5s ease-in-out;
  }

  .UltraDiv:not(:hover) {
    transform: translateY(0);
  }

</style>
</head>
<body>

    <div id="header">
	<a href="/site.html" title="Back"><img src="/assets/back.png" style="float:left; margin-block-start: 0.67em;
        margin-block-end: 0.67em; width: auto; height: auto; max-width: 60px;max-height: 60px""></a>
        <h1>ChatGPT Client</h1>
    </div>
    <div class="UltraDiv">
    <div id="container"> ''' + form1 + '''</div>
    <br>
''' + answer + '''
</div>
<div class="copyright">
    <a href="/cgi-bin/chatgpt.py?action=%21reboot" title="!reboot">
    <h3>Перезапуск нейросети</h3>
    </a>
  </div>
<div class="img">
    <img src="/assets/yoptai.png" class="yopta">
</div>
</body>
</html>
'''

print('Content-type: text/html\n')
print(pattern)


