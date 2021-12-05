
import math

def pwr(p):
  def numpower(n):
    return n**p
  return numpower

commands = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), "модуль": abs, "синус": math.sin}

n = int(input())
command = input()
print(commands[command](n))
