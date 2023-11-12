# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:26:42 2021

@author: sidvs
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:48:34 2021

@author: sidvs
"""
import random
import string
import time
from threading import Thread

symbols = []
symbols = list(string.ascii_uppercase)
card1 = [0]*11
card2 = [0]*11
pos1 = random.randint(0,10)
pos2 = random.randint(0,10)
print(pos1)
print(pos2)

# pos1 & pos2 are same symbol positions in card1 & card2 respectively

samesymbol  = random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
    
i=0
while(i<11):
    if(i!=pos1 and i!= pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)

ch = None

def check():
    time.sleep(5)
    if (ch!=None):
        return
    print("Too slow! No points")
Thread(target=check).start()    
ch=input("Spot the similarity ")


if(ch==samesymbol):
    print("Right")
else:
    print("Wrong")