tu=(1,2,3,4,5)# syntax for tuple
tup=() # empty tuple
tupl=(1,)  # single element tuple, note the comma
print(tu)
print(type(tu))  # Output: <class 'tuple'>
#function of tuple
print(tu.count(2))  # Count occurrences of 2 in the tuple
print(tu.index(3) ) # Find the index of the first occurrence of 3


# Tuples are immutable, so we cannot change their elements
# tu[0] = 10  # This will raise a TypeError 
# However, we can concatenate tuples
new_tu = tu + (6, 7)  # Concatenating a tuple
print(new_tu)  # Output: (1, 2, 3, 4, 5, 6, 7)