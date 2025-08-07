# syntax of string 
name="sachin kumar"
nameshort=name[0:3]
print(nameshort)


#string slicing
name1="sachin kumar"
print(name1[0:5])  # prints 'sachi' 
print(name1[6:11])  # prints 'kumar'
print(name1[0:11:2])  # prints 'sai uar'
print(name1[::])  # prints 'sachin kumar'
print(name1[::-1])  # prints 'ramuk nihcas' 
# string concatenation
name2="sachin"
name3="kumar"
name4=name2 + " " + name3
print(name4)  # prints 'sachin kumar'
# string repetition
name5="sachin"
name6=name5 * 3
print(name6)  # prints 'sachinsachinsachin'
# string length
name7="sachin kumar"
print(len(name7))  # prints 12
# string methods
name8="sachin kumar"
print(name8.upper())  # prints 'SACHIN KUMAR'
print(name8.lower())  # prints 'sachin kumar'
print(name8.title())  # prints 'Sachin Kumar'
print(name8.replace("sachin", "rahul"))  # prints 'rahul kumar'
print(name8.find("kumar"))  # prints 6 (index of 'kumar')
print(name8.split())  # prints ['sachin', 'kumar']
# string formatting
name9="sachin"
age=30
print(f"My name is {name9} and I am {age} years old.")
# prints 'My name is sachin and I am 30 years old.'
print("My name is {} and I am {} years old.".format(name9, age))
