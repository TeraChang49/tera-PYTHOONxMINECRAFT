from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
print(mcs.player.getTilePos())
x=200
y=75
z=100
mcs.player.setTilePos(x,y,z)
