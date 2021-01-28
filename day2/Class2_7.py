from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
while True:
    num=0
    try:
        num=int(input('what do you want?'))
    except:
        print("That is not number.")
    x,y,z=mcs.player.getTilePos()
    mcs.setBlock(x,y,z,num)
    e=input("Exit?")
    if e=="yes":
        break
    else:
        continue