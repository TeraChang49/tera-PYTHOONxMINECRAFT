from mcpi.minecraft import Minecraft as mc
import time
import random
mc=mc.create()
x,y,z=mc.player.getPos()
while True:
    time.sleep(1)
    x=x+random.uniform(-20,20)
    y=y+random.uniform(-20,20)
    z=z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,93)