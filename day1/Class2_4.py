from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
s=20
mcs.setBlocks(x+s,y,z+s,x-s,y+s,z-s,0)