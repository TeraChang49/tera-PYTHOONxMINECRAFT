from mcpi.minecraft import Minecraft as mc
mc=mc.create()
line1=[]
line2=[]
line3=[]
for i in range(1,4):
    line1.append(i*1)
for i in range(1,4):
    line2.append(i*2)
for i in range(1,4):
    line3.append(i*3)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))