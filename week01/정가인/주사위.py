a=0
b=0
c=0
score=0
import random
a= random. randint(1,6)
b= random. randint(1,6)
c= random. randint(1,6)
print(f"{a} {b} {c}")
if a==b :
  if b==c:
    score += 10000
    score += a * 1000
    print(score)
  else : 
    score += 1000
    score += a*100
    print(score)
else : 
  if b==c:
    score += 1000
    score += b*100
    print(score)
  if a==c:
    score += 1000
    score += a*100
    print(score)
  else : 
    score = max(a,b,c)*100
    print(score)