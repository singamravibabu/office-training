# # List Object

# ### List Methods

# %%
emps = ["Raju", "Srinu", "Kumar", "Anil", "Kavya", "Ankita", "Praveena"]

# %%
# 1. append(item): Adds an item to the end of the list.

# %%
emps.append("Suresh")     # object.method(argument)
emps

# %%
emps.append("Sunitha")
emps

# %%
# 2. insert(index, item): Inserts an item at a specified index.

# %%
emps

# %%
emps.insert(0, "Guru")
emps

# %%
emps.insert(5, "Sarala")
emps

# %%
emps.append("Kumar")

# %%
emps.append("Suresh")

# %%
emps

# %%
# 3. remove(item): Removes the first occurrence of an item from the list.

# %%
emps.remove("Kumar")
emps

# %%
# 4. index(item): Returns the index of the first occurrence of an item.

# %%
emps.index("Suresh")

# %%
emps.index("Ankita")

# %%
# 5. pop([index]): Removes and returns the item at the specified index. If no index is specified, it removes and returns the last item.

# %%
emps

# %%
emp_name = emps.pop(4)
emp_name

# %%
emps

# %%
emps.pop(12)

# %%
emps

# %%
emps.pop()  # removes last item

# %%
emps

# %%
emps.pop() # removes last item

# %%
emps

# ### len() for getting the lenght of a list / tuple / array / dict / string

# %%
len(emps)

# ### The `in` keyword to check whether an item is in the list

# %%
'''
item in list
item in tuple
item in dict
item in string
'''
# If the `item` is in the `list`, it returns True; otherwise, it returns False.

# %%
'Kavya' in emps
if 'Kavya' in emps:
    print("Kavya is working presently with us.")

# %%
emp = "Naveen"
if emp in emps:
    print(f"{emp} is working presently with us.")
else:
    print(f"{emp} is not working presently with us.")

# %%
'Guru' in emps

# %%
'Nagaraju' in emps

# ### Printing items in a list

# %%
print(emps)     ### Printing items in a list

# ### Looping through items in a list

# %%
for e in emps:
    print(e, end="  ")     ### Looping through items in a list

# ### List are mutable (changable)

# - List is a mutable object (changeable - add, remove, update items)
# - Str, int, float, bool, tuple, ... are immutable objects

# %%
print(emps)

# %%
emps[1] = "Vivek"
emps

# ### List of list (somewhat like matrix)

# - A list where its items are lists, and such list is a list of list
# - A list of lists is also called as two-dimensional list (matrix)

# %%
# matrix (list of lists) with 3 rows and 5 columns
students = [
    ["Raju", 23, "A+" , "Maths", "Science"],
    ["Srinu", 22, "B" , "English", "Social"],
    ["Kumar", 24, "A" , "Physics", "Chemistry"]
]

# %%
students[0]  # first row

# %%
students[1] # second row

# %%
students[2] # third row

# %%
students[0][4]  # first row, fifth column

# %%
students[1][4] # second row, fifth column

# %%
students[2][4] # third row, fifth column

# %%
for student in students:
    print(student[0].ljust(10), student[2])

# %%
students[0][0].ljust(10) + students[0][2]

# ### More skills to work with lists

# %%
# 1. count(item): Returns the number of occurrences of an item in the list.

# %%
print(emps)

# %%
emps.count("Guru")

# %%
emps.count("Vivek")

# %%
emps.count("Babu")

# %%
# 2. reverse(): Reverses the order of items in the list.

# %%
emps
emps.reverse()
emps

# %%
# 3. sort([key=function]): Sorts the items of the list in ascending order by default.
# We can also apply a function to sort the items.

# %%
emps.insert(3, "anand")
print(emps)

# %%
emps.sort()
print(emps)

# %%
emps.sort(key=str.lower)        # emps.sort(key=str.upper)
print(emps)

# %%
# sorted(list[, key=function][reverse=True])
# The sorted() function returns a new sorted list from the items in the given iterable without modifying the original iterable.

# %%
emp_new_list = sorted(emps, reverse=True, key=str.lower)
print(emp_new_list)

# ### Two built-in functions: min() and max()

# %%
numbers = [34, 1, 0, -23, 12, 99, 4, -55, 67]
print(numbers)

# %%
max(numbers)

# %%
min(numbers)

# ### The 'random' module functions: choice(), & shuffle()

# %%
print(numbers)

# %%
# import random module and use the choice() function to choose an item from a list randomly
import random

# %%
random.choice(numbers) # homework: run this cell multiple times to see different outputs

# %%
# shuffle() function from random module to shuffle the items of a list randomly
random.shuffle(numbers)
print(numbers)

# ### Copying lists
# - The assignment operator makes a shallow copy of a list, so both list variables refer to the same list.
# - In contrast, the `deepcopy()` function form `copy` module makes a deep copy of a list, and variables refere to the two different lits.

# %%
m = [1, 2, 3]
n = m

# %%
m[0] = 100
m

# %%
n

# %%
import copy
a = [1, 2, 3]
b = copy.deepcopy(a)

# %%
a[0] = 100
a

# %%
b

# %%
b[0] = 200
b

# %%
a

# ### Slicing the list
# - list[start:end:step]

# %%
nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# %%
nums[0:4] # first four items

# %%
nums[2:8]  # from index 2 to index 7

# %%
nums[::2] # every second item

# %%
nums[1::2] # every second item starting from index 1

# %%
nums[::-1]  # reversing the list

# %%
nums[::3] # every third item


