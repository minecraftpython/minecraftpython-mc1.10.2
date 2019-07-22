#name<=>Puppies!
#cooldown<=>20000
#texture<=>lead
import random
def spawnentity_yscandown(x,y,z,entityType=PIG,forceTheIssue=True,scanDistance=10,entityNbt=''):
	yOrig=y
	while(getblock(x,y-1,z) == AIR):
		y-=1
		if(forceTheIssue == False and yOrig-y>scanDistance):
			break
	spawnentity(x,y,z,entityType,nbtData=entityNbt)
	return y


def puppies(x,y,z,radius=5,puppies=5,ownerName='',timeBetween=2):
	for n in range(puppies):
		yell('Puppy!')
		pupX = random.choice(range(x-radius,x+radius))
		pupZ = random.choice(range(z-radius,z+radius))
		pupY = spawnentity_yscandown(pupX,y+radius,pupZ,WOLF,entityNbt='{Owner:'+ownerName+'}')
		spawnparticle(pupX,pupY,pupZ,10,HEART)
		time.sleep(timeBetween)
puppies(myX(),myY(),myZ(),ownerName=_get_player_name())