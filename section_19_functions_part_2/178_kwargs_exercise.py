def combine_words(s, **kwargs):
   if 'prefix' in kwargs:
      return kwargs['prefix'] + s
   elif 'suffix' in kwargs:
      return s + kwargs['suffix']
   return s

print(combine_words('child')) # child
print(combine_words('child', prefix='man')) # manchild
print(combine_words('child', suffix='ish')) # childish
print(combine_words('work', suffix='er')) # worker
print(combine_words('work', prefix='home')) # homework