'''
* Copyright (c) 2013-2015 GameStart LLC
* Distributed under the GNU GPL v2. For full terms see the file LICENSE.
'''

import socket
import mcpi.minecraft as minecraft
from mcpi.block import *
import random as random
import time

__author__ = 'gamestart'
MINECRAFT_SERVER = 'localhost'
TNT = Block(TNT.id, 1)

def get_server_name():
    return MINECRAFT_SERVER

mc = minecraft.Minecraft.create()
mc_server = minecraft.Minecraft.create(get_server_name())

def setblock_at_pos(pos, blocktype=DIRT):
    setblock(pos.x, pos.y, pos.z, blocktype)

def setblock(*args):
    mc_server.setBlock(*args)

def cube(px, py, pz, blocktype, size):
    size = min(size, 12)
    for x in range(size):
        for y in range(size):
            for z in range(size):
                mc_server.setBlock(x + px, y + py, z + pz, blocktype)

def teleport_at_pos(pos):
    teleport(pos.x, pos.y, pos.z)

def teleport(x, y, z):
    mc.player.setPos(x, y, z)

def my_pos():
    return mc.player.getPos()

class Player():
    def __init__(self, mc_player):
        self.mc_player = mc_player

    @property
    def position(self):
        return self.mc_player.getPos()

    @property
    def x(self):
        return self.mc_player.getPos().x

    @property
    def y(self):
        return self.mc_player.getPos().y

    @property
    def z(self):
        return self.mc_player.getPos().z

player = Player(mc.player)

def pick_random_player():
    listOfPlayerEntityIds = mc_server.getPlayerEntityIds()
    print("Players: " + str(len(listOfPlayerEntityIds)))
    chosenPlayerId = random.choice(listOfPlayerEntityIds)
    print("Player to report position" + str(chosenPlayerId))
    return chosenPlayerId

def yell(stringToYell):
    mc.postToChat(stringToYell)

print "Starting..."

