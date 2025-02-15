

import random

lenth=random.randint(8,12) 

sambol=['!','@','#','$','%','^','&','*','(',')','_','-','=','+',
        '/','?','~']
lenth_sambol=None
if lenth==8:
    lenth_sambol=random.randint(1,2)
elif lenth>=9 and lenth<=11:
    lenth_sambol=random.randint(2,3)
else:
    lenth_sambol=random.randint(2,3)  

lower=['q','w','r','t','y','u','i','i','o','p','a','s','d','f','g','h','j','k','l',
        'z','x','c','v','b','n','n','m',' ']
lenth_lower=None
if lenth==8:
    lenth_lower=random.randint(1,2)
elif lenth>=9 and lenth<=11:
    lenth_lower=random.randint(2,3)
else:
    lenth_lower=random.randint(3,4)  

number=['0','1','2','3','4','5','6','7','8','9'] 
lenth_number=None
if lenth==8:
    lenth_number=random.randint(1,2)
elif lenth>=9 and lenth<=11:
    lenth_number=random.randint(2,3)
else:
    lenth_number=random.randint(3,4)  

captal=[] 
lenth_captal=None  
for l in lower:
    captal.append(l.upper()) 

lenth_captal=lenth-(lenth_sambol+lenth_lower) 

result=''
for q in range(lenth_sambol):
    result+=random.choice(sambol) 

for q in range(lenth_lower):
    result+=random.choice(lower) 

for q in range(lenth_number):
    result+=random.choice(number) 

for q in range(lenth_captal):
    result+=random.choice(captal) 

result=''.join(reversed(result)) 
temp=list(result) 
random.shuffle(temp) 
random.shuffle(temp) 
random.shuffle(temp)
random.shuffle(temp) 
random.shuffle(temp) 
random.shuffle(temp) 
random.shuffle(temp) 
random.shuffle(temp) 

result=''
for q in temp:
    result+=q 

print(result) 

