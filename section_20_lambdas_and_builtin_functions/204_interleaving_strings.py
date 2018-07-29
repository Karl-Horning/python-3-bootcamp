def interleave(str1, str2):
   # return ''.join(str(l) for l in (zip(str1, str2)))
   return ''.join(''.join(l) for l in (zip(str1, str2)))

print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr', 'iad'))