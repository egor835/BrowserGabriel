#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import os.path

a="kek"
path = "files"
for file in os.path.walk(path):
    if file.name.startswith("."):
        a = a+file.path
print('Content-type: text/html\n')
print(a)
