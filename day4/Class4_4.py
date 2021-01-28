from mcpi.minecraft import Minecraft as mc
import time
import random
mc=mc.create()
x,y,z=mc.player.getTilePos()
com=random.randint(0,15)
for i in range(20):
    for j in range(20):
        color=random.randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==com:
            mc.postToChat("You are right")
            break
        else:
            mc.postToChat("Try again")