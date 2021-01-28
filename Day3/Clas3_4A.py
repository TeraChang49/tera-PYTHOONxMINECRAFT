from mcpi.minecraft import Minecraft as mc
mc=mc.create()
x,y,z=mc.player.getTilePos()
def planttree(x,y,z,mc):
    mc.setBlocks(x-1,y+4,z-1,x+1,y+7,z+1,35,5)
    mc.setBlocks(x,y,z,x,y+4,z,17)
for i in range(5):
    planttree(x+i*5,y,z,mc)
    