# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:09:36 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time
wand=Minecraft.create()
while True:
    x,y,z = wand.player.getTilePos()
    wand.setblock(x,y,z,0407)