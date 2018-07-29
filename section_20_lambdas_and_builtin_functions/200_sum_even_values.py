def sum_even_values(*args):
   return sum(n for n in args if n % 2 == 0)

print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10))
print(sum_even_values(1))