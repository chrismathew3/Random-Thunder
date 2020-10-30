import requests
import time
from PIL import Image

def randomOrgCall(num,min_n=0,max_n=255):
	url="https://www.random.org/integers/?num={num}&min={min_n}&max={max_n}&col=1&base=10&format=plain&rnd=new".format(num=str(num),min_n=str(min_n),max_n=str(max_n))
	nums = ''
	while nums == '':
	    try:
	        nums = requests.get(url)
	        break
	    except:
	        print("Connection refused by the server..")
	        print("Let me sleep for 5 seconds")
	        print("ZZzzzz...")
	        time.sleep(5)
	        print("Was a nice sleep, now let me continue...")
	        continue
	return list(map(int, nums.text.strip().split("\n"))) 

def get_rgb():
	total_px=120*120*3 								#for RGB tuples
	px=[]
	for _ in range (5): 							#total_px/max number allowed(10000)		
		n= 10000 if total_px>10000 else total_px	#max number allowed by random.org
		random_nums= randomOrgCall(n)
		total_px-=10000
		px = px+random_nums

	ret=[]
	for i in range(0,len(px),3):
		temp_tuple=(px[i],px[i+1],px[i+2])
		ret.append(temp_tuple)

	return ret


image_size = (120, 120)
# create new image
im = Image.new(mode="RGB", size=image_size)
#get RGB tuples
im.putdata(get_rgb())
#show and save image
im.show()
im.save("random_bitmap.jpg")

