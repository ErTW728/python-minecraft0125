# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:24:09 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time
wand=Minecraft.create()
i = 0
while True:
    i = i+1
    wand.postToChat("第"+str(i)+"次")
    time.sleep(1)