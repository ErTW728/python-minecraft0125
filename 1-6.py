# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:37:20 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time
wand=Minecraft.create()
wand.postToChat("I'm watching u")
while True:
    x,y,z = wand.player.getTilePos()
    wand.postToChat("X:"+ str(x) +"Y:" +str(y) +"Z:" +str(z))
    time.sleep(0.1)