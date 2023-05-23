from revChatGPT.V3 import Chatbot
import os
import time
t = open("../token", "r")
token = t.read()
t.close()
chatbot = Chatbot(api_key=token, engine="gpt-3.5-turbo")
while True:
    while os.path.isfile("input.txt") == False:
        pass
    time.sleep(0.5)

    f = open("input.txt", "r")
    text = f.read()
    f.close()
    os.remove("input.txt")
    print(text)
    if text == "!reset":
        chatbot.reset()
        response = "clear"
    elif text == "":
        response = ""
    elif text == "!clear":
        response = "clear"
    else:
        response = chatbot.ask(text)
    print(response)

    if response == "" or response == "clear":
        f = open("output.txt", "w")
        f.write(response)
        f.close()
    else:
        f = open("output.txt", "w")
        f.write(f"Bot: {response}<br><br>User: {text}<br>-----------------<br>")
        f.close()
