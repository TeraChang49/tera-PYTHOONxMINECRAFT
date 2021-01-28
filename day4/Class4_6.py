from mcpi.minecraft import Minecraft as mc
from time import sleep
import random
mc=mc.create()
myID=mc.getPlayerEntityId("60109tera")
mineral=[14,15,16,21,56,73,129]
while True:
    sleep(0.5)
    r=random.choice(mineral)
    x,y,z=mc.entity.getTilePos(myID)
    mc.setBlocks(x+1,y,z+1,x-1,y+3,z-1,r)