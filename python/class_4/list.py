friends=["apple", "banana", "cherry", "date"]
#unlike a tuple, a list is mutable
print(friends[0])  # Output: apple
friends[0] = "avocado"  # Changing the first element
print(friends)  # Output: ['avocado', 'banana', 'cherry',   'date']
friends.append("elderberry")  # Adding a new element        

#function of  list
friends.sort()  # Sorting the list
print(friends)  # Output: ['avocado', 'banana', 'cherry', 'date', 'elderberry']
friends.reverse()  # Reversing the list
print(friends)  # Output: ['elderberry', 'date', 'cherry', 'banana', 'avocado']
friends.remove("banana")  # Removing an element
print(friends)  # Output: ['elderberry', 'date', 'cherry', 'avocado']
friends.pop()  # Removing the last element  
print(friends)  # Output: ['elderberry', 'date', 'cherry']
friends.clear()  # Clearing the list    
print(friends)  # Output: []
friends = ["apple", "banana", "cherry"]  # Reinitializing the list
# List slicing
print(friends[1:3])  # Output: ['banana', 'cherry']
# List comprehension
squared_numbers = [x**2 for x in range(10)]  # Creating a list of squared numbers
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List concatenation
new_friends = friends + ["date", "elderberry"]  # Concatenating two lists
print(new_friends)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# List repetition
repeated_friends = friends * 2  # Repeating the list
print(repeated_friends)  # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
# Checking membership   
print("apple" in friends)  # Output: True
print("fig" in friends)  # Output: False    
# Finding the index of an element
print(friends.index("banana"))  # Output: 1
# Finding the count of an element
print(friends.count("apple"))  # Output: 1
# Finding the length of the list
print(len(friends))  # Output: 3
# Finding the maximum and minimum elements
print(max(friends))  # Output: cherry
print(min(friends))  # Output: apple
# Finding the sum of a list of numbers
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15
# Finding the average of a list of numbers
average = sum(numbers) / len(numbers)
print(average)  # Output: 3.0
# Finding the first and last elements   