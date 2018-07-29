def max_magnitude(l):
   return max(abs(n) for n in l)

print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))