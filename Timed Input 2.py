# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:41:19 2021

@author: sidvs
"""


#If it is acceptable to block the main thread when user haven't provided an answer:

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt = "You have %d seconds to choose the correct answer...\n" % timeout
answer = input(prompt)
t.cancel()

