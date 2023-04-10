#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import os
import time

class Fetch:
    def __init__(self):
        return

    def cre(self, txt):
        f = open("input.txt", "w")
        f.write(txt)
        f.close()

    def read(self):
        while os.path.isfile("output.txt") == False:
            pass
        time.sleep(0.5)
        f = open("output.txt", "r")
        output = f.read()
        f.close()
        os.remove("output.txt")
        f = open("history.txt", "r")
        his = f.read()
        f.close()
        text = output + his
        f = open("history.txt", "w")
        f.write(text)
        f.close()
        return text