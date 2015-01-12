import socket
import mcpi.minecraft as minecraft
from mcpi.block import *
import random as random
import time

__author__ = 'gamestart'
MINECRAFT_SERVER = 'localhost'
TNT = Block(TNT.id, 1)

def get_ip_postfix():
    return int(socket.gethostname().lstrip('pi'))


def is_hosting_minecraft():
    return bool(get_ip_postfix() % 2)  #Odd numbers host Minecraft for the previous Pi


def get_server_name():
    return MINECRAFT_SERVER or "192.168.3.%s" % ((((int(get_ip_postfix()) - 1) / 4) ) * 4 + 1)


local_mincraft = minecraft.Minecraft.create()
server_minecraft = minecraft.Minecraft.create(get_server_name())


def setblock_at_pos(pos, blocktype=DIRT):
    setblock(pos.x, pos.y, pos.z, blocktype)


def setblock(*args):
    server_minecraft.setBlock(*args)


def cube(px, py, pz, blocktype, size):
    size = min(size, 12)
    for x in range(size):
        for y in range(size):
            for z in range(size):
                server_minecraft.setBlock(x + px, y + py, z + pz, blocktype)


def teleport_at_pos(pos):
    teleport(pos.x, pos.y, pos.z)


def teleport(x, y, z):
    local_mincraft.player.setPos(x, y, z)


def my_pos():
    return local_mincraft.player.getPos()

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

player = Player(local_mincraft.player)

def pick_random_player():
    listOfPlayerEntityIds = server_minecraft.getPlayerEntityIds()
    print("Players: " + str(len(listOfPlayerEntityIds)))
    chosenPlayerId = random.choice(listOfPlayerEntityIds)
    print("Player to report position" + str(chosenPlayerId))
    return chosenPlayerId


def yell(stringToYell):
    local_mincraft.postToChat(stringToYell)

print "Starting..."
