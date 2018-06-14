dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

double_dict1 = {k:v*2 for (k,v) in dict1.items()}

# Solving problems using dictionary comprehension

# Using a For loop
numbers = range(10)
new_dict_for = {}

for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2

# Using Dictionary Comprehsnsive
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_for)
print(new_dict_comp)