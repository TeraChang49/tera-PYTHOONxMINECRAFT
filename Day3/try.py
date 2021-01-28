from mcpi.minecraft import Minecraft as mc
mc=mc.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x, hit.pos.y, hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.setBlock(x,y,z,20)


