set1 = {1,2,3,4,4,4}

set1.add(5)
print(set1)

# union(), intersection(), difference(), symmertic_difference()
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))