#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import os
import time

class Fetch:
    def __init__(self):
        return

    def cre(self, txt):
        if os.path.isfile("generating_gpt") == False and txt != "" and txt != " " and txt != "  ":
            f = open("input.txt", "w")
            f.write(txt)
            f.close()

    def read(self):
        f = open("history_gpt.txt", "r")
        text = f.read()
        f.close()
        return text
