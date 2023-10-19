import pexpect
import time
from translate import Translator
import os
import js
config = js.get_config()
eng = Translator(from_lang="en", to_lang="ru")
rus = Translator(from_lang="ru", to_lang="en")
try:
    os.remove("ready")
    os.remove("generating")
except:
    time.sleep(0)
print("Llama.cpp (re)started")
cmd = f"./llama.cpp/main -m ./files/models/{config['model']} -n {config['n']} --repeat_penalty {config['penalty']} {config['args']} --color -i -r \"User:\" -f ./files/prompts/{config['prompt']}"
print(cmd)
child = pexpect.spawn(cmd)
for x in range(config['skips']):
    child.expect('User:')
time.sleep(config['sleep_time'])
open("ready", 'a').close()
print("Llama.cpp ready")
child.expect("User:")
while True:
    while os.path.isfile("h_input.txt") == False:
        pass
    time.sleep(0.5)
    f = open("h_input.txt", "r")
    line = f.read()
    f.close()
    os.remove("h_input.txt")
    if line == "!reboot":
        child.terminate()
        try:
            os.remove("ready")
        except:
            time.sleep(0)
        config = js.get_config()
        cmd = f"./llama.cpp/main -m ./files/models/{config['model']} -n {config['n']} --repeat_penalty {config['penalty']} {config['args']} --color -i -r \"User:\" -f ./files/prompts/{config['prompt']}"
        print("Llama.cpp (re)started")
        print(cmd)
        child = pexpect.spawn(cmd)
        for x in range(config['skips']):
            child.expect('User:')
        time.sleep(config['sleep_time'])
        open("ready", 'a').close()
        print("Llama.cpp ready")
        child.expect("User:")
        f = open("history.txt", "w")
        f.write("Rebooted")
        f.close()
    else:
        open("generating", 'a').close()

        if config['use_translator'] == True:
            tr_line = rus.translate(line.replace(',', ''))
            if "QUERY LENGTH LIMIT EXCEEDED" in tr_line:
                tr_line = line
            print(f'{line} - {tr_line}')
        else:
            tr_line = line
            print(line)

        child.sendline(tr_line)
        hist = f"User: {line}<br>-----------------<br>"
        f = open("history.txt", "r")
        older = f.read()
        f.close()
        text = hist + older
        f = open("history.txt", "w")
        f.write(text)
        f.close()

        child.expect("\n", timeout=999999)
        child.expect('User:', timeout=999999)
        output = child.before.decode("utf-8")
        output = output.replace("Gab:", "", 1)
        output = output[1:]
        output = output.replace("[0m", "")

        if config['use_translator'] == True:
            response = eng.translate(output)
            if "QUERY LENGTH LIMIT EXCEEDED" in response:
                response = output
            print(f'{output} - {response}')
        else:
            response = output
            print(response)

        try:
            os.remove("generating")
        except:
            time.sleep(0)
        hist = (f"Gab: {response}<br><br>")
        f = open("history.txt", "r")
        older = f.read()
        f.close()
        text = hist + older
        f = open("history.txt", "w")
        f.write(text)
        f.close()

