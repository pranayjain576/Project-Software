import random 
from playsound import playsound
list=[]
i=0
while (i<20):
  n = random.randint(1, 20)  
  if(n not in list):
      list.append(n)
      print("Sound no. "+ str(n)+ " is being played")
      url="music\\" +str(n)+".mp3"
      playsound(url)

  else:
      continue
  i=i+1

