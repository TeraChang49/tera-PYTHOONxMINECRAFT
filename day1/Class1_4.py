from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()
x,y,z=mcs.player.getPos()
i=0
while i < 5:
    mcs.player.setTilePos(x,y,z)
    time.sleep(1.5)
    y=y-10

 
