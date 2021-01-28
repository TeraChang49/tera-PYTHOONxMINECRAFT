from mcpi.minecraft import Minecraft as mc
mc=mc.create()
x,y,z=mcs.player.getPos()
for i in range (40):
    mc.setBlock(x+i,y+i,z+i,57)