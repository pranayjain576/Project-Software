import random 
from playsound import playsound
list=[]
i=0
while (i<20):
  n = random.randint(1, 20)  
  if(n not in list):
      list.append(n)
      url="C:\\Users\\Pranay\\Desktop\\Python\\music\\" +str(n)+".mp3"
      playsound(url)
  else:
      continue
  i=i+1

print(list)