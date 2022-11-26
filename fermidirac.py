def distribute(e, n):
  dist = {};
  for i in range(0,e+1):
    dist[f"L{i}"] = []
    for j in range(1,n+1):
      dist[f"L{i}"].append(j)
  return dist

e = int(input("Energy levels:"))
n = int(input("Particles:"))

print(distribute(e,n))
