from revChatGPT.V3 import Chatbot
import os
import time
t = open("../key", "r")
token = t.read().replace("\n","")
t.close()
print(token)
chatbot = Chatbot(api_key=token, engine="gpt-3.5-turbo")
try:
    os.remove("generating_gpt")
except:
    time.sleep(0)
print("started")
while True:
    while os.path.isfile("input.txt") == False:
        pass
    time.sleep(0.5)
    f = open("input.txt", "r")
    prompt = f.read()
    f.close()
    os.remove("input.txt")
    if prompt == "!reboot":
        print("rebooting")
        chatbot.reset()
        f = open("history_gpt.txt", "w")
        f.write("Rebooted")
        f.close()
    else:
        print(prompt)
        open("generating_gpt", 'a').close()
        hist = f"User: {prompt}<br>-----------------<br>"
        f = open("history_gpt.txt", "r")
        older = f.read()
        f.close()
        text = hist + older
        f = open("history_gpt.txt", "w")
        f.write(text)
        f.close()
        output = chatbot.ask(prompt)
        try:
            os.remove("generating_gpt")
        except:
            time.sleep(0)
        hist = (f"GPT: {output}<br><br>")
        f = open("history_gpt.txt", "r")
        older = f.read()
        f.close()
        text = hist + older
        f = open("history_gpt.txt", "w")
        f.write(text)
        f.close()

        print(output)
