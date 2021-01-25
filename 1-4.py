# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:53:27 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time
wand=Minecraft.create()
x = 200
y = 200
z = 100
wand.player.setPos(x,y,z)
time.sleep(2)
x = x-50
y = y-50
wand.player.setPos(x,y,z)
time.sleep(2)
x = x-50
y = y-50
wand.player.setPos(x,y,z)
time.sleep(2)
x = x-50
y = y-50