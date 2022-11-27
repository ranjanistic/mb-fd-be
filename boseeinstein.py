from random import randint
from functools import reduce

def distribute(e, n):
  dist = {}
  for i in range(0,e+1):
    dist[f"L{i}"] = []
  for p in range(1,n+1):
    x = n
    for i in range(0,e+1):
      x = randint(0,x)
      dist[f"L{i}"].append(x)
      if reduce(lambda z,y:z+y, dist[f"L{i}"]) >= n:
        break
      else:
        x = n - x
  return dist

#eunits = int(input("Energy units:"))
#particles = int(input("Particles:"))

print(distribute(7,9))
