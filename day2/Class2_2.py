from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
s=2
mcs.setBlocks(x+1,y+3,z+1,x-1,y+3,z-1,20)
mcs.player.setPos(x,y+4,z)
mcs.setBlocks(x+s,y,z+s,x-s,y+1,z-s,11)