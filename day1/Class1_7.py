from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
#mcs.setBlock(x+1,y,z,15)
#mcs.setBlock(x-1,y,z,15)
#mcs.setBlock(x,y,z+1,15)
#mcs.setBlock(x,y,z-1,15)
#mcs.setBlock(x-1,y,z-1,15)
#mcs.setBlock(x+1,y,z+1,15)
#mcs.setBlock(x-1,y,z+1,15)
#mcs.setBlock(x+1,y,z-1,15)
s=20
mcs.setBlocks(x+s,y,z+s,x-s,y+s,z-s,0)