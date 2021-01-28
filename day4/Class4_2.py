from mcpi.minecraft import Minecraft as mc
mc=mc.create()
x,y,z=mc.player.getTilePos()
num=1
for i in range(8):
    for j in range(num):
        mc.spawnEntity(x,y,z,60)
    num=num*2
    mc.postToChat("borned"+str(num)+"fish")