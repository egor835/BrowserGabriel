#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import os


class Fetch:
    def __init__(self):
        return
    def cre(self, txt):
        if os.path.isfile("generating") == False and txt != "" and txt != " " and txt != "  ":
            f = open("h_input.txt", "w")
            f.write(txt)
            f.close()

    def read(self):
        f = open("history.txt", "r")
        text = f.read()
        f.close()
        return text
