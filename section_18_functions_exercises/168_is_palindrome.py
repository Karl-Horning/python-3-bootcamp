def is_palindrome(string):
   string = string.replace(' ', '').lower()
   return string == string[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True
print(is_palindrome('a man a plan a canal Panama'))