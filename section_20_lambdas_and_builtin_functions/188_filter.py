l = [1,2,3,4]
names = ['Austin', 'Penny', 'Anthony', 'Angel', 'Billy']
new_names = ['Colt', 'Rusty', 'Lassie']

evens = list(filter(lambda i: i % 2 ==0, l))
a_names = list(filter(lambda n: n[0].lower() == 'a', names))
four_letter_names = list(map(lambda n: f'Your instructor is {n}', 
                    filter(lambda n: len(n) < 5, new_names)))
four_letter_names2 = [f'Your instructor is {name}' for name in new_names if len(name) < 5]

print(evens) # [2, 4]
print(a_names)
print(four_letter_names)
print(four_letter_names2)