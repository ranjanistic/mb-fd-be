from math import factorial as fact

class console():
  def log(*args):
    print(*args)

q = int(input("Energy units: ")) # 9
N = int(input("Particles: ")) # 6

p = int(fact(q+N-1)/(fact(q)*fact(N-1)))

console.log(p, "microstates")


console.log("\n")
