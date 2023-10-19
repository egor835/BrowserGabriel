#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import edit
import os
config = edit.get_config()
write = edit.write_config
form = cgi.FieldStorage()


for n in config.keys():
    val = form.getfirst(n)
    print(str(val))
    if val == None or val == "":
        pass
    elif val == "True" or val == "true":
        config[n] = True
    elif val == "False" or val == "false":
        config[n] = False
    elif type(config[n]) != str:
        try:
            config[n] = int(val)
        except:
            config[n] = config[n]
    else:
        config[n] = val

write(config)

finform = f'''
            <br>
            <div id=label>
            Available models: 
            </div>
            {str(os.listdir("files/models")).replace("'", "").replace("]", "").replace("[", "").replace(",", "<br>")}
            <br>
            <br>
            <div id=label>
            Available prompts: 
            </div>
            {str(os.listdir("files/prompts")).replace("'", "").replace("]", "").replace("[", "").replace(",", "<br>")}
            <br>
            <br>'''
for n in config.keys():
    finform = finform + f'''
        <div id=label>
        {n}: 
        </div>
        <input type="text" id="action" name="{n}" value="{config[n]}">
        <br>
        '''

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Config page</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f8fa;
        margin: 0;
        padding: 0;
        text-align: right;
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
    
    #action {
        width: 600px;
        padding: 5px;
        margin: auto;
        display:inline-block;
    }
    #subm {
    text-align: center;
    }

    #label {
    text-align: left;
    float:left
    }

    #submit-button {
        background-color: #000000;
        color: #fff;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 3px;
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
        <h1>Bot configuration</h1>
    </div>
    <div class="UltraDiv">
        <div id="container"> 
        <form id="user-input" action="/cgi-bin/config.py">
    '''+ finform + '''
    <div id=subm>
    <br>
    <button type="submit" id="submit-button">Apply</button>
    </div>
    </form>
    </div>
</body>
</html>

'''

print('Content-type: text/html\n')
print(pattern)
