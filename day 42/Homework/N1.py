numbers={1,1,2,3,4,5}
even_numbers=(2,4,6,8,10)

numbers.add(6)
numbers.remove(3)
print(numbers)

union=numbers.union(even_numbers)
print(union)

difference= numbers.difference(even_numbers)
print(difference)

intersection=numbers.intersection(even_numbers)
print(intersection)