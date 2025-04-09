# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

print("Create a list and assign it to a variable")
coffee_list = ["Latte", "Americano", "Flat white", "Espresso"]


print("Find the length of the list")
print(len(coffee_list))


print("Append an item to the list")
coffee_list.append(1)
print(coffee_list)


print("Find the value of an item in the list a specific index")
print(coffee_list[1])


print("Set the value of an item at a specific index")
coffee_list[4] = "Cappuccino"
print(coffee_list)


print("Check whether an item is in the list")
if "Latte" in coffee_list:
    print("found")


print("Sort the list without sort method")
#coffee_list.sort()
new_list = [1, 3, 5, 6, 0, 9]
i = 1
while i < len(new_list):
    to_insert = new_list[i]
    insertion_index = i
    while insertion_index > 0 and new_list[insertion_index - 1] > to_insert:
        new_list[insertion_index] = new_list[insertion_index - 1]
        insertion_index -= 1
    new_list[insertion_index] = to_insert
    i += 1

print(new_list)



print("Iterate over the list using range, printing out each element and the index")
for i in range(len(coffee_list)):
    print(f"{i} : {coffee_list[i]}") 


print("Iterate over the list without using range, printing out each element")
for items in coffee_list:
    print(items)


'''TUPLES'''

print("Create a tuple and assign it to a variable")
tupple_1 = ("apple", "banana", "orange")
print(tupple_1)


print("Find the length of the tuple")
print(len(tupple_1))


print("Find the value of an item in the tuple a specific index")
print(tupple_1[0])


print("Check whether an item is in the tuple")
print("apple" in tupple_1)
print(type(tupple_1))


print("Iterate over the tuple using range, printing out each element and the index")
for i in range(len(tupple_1)):
    print(f"{i} : {tupple_1[i]}")


print("Iterate over the tuple without using range, printing out each element")
for items in tupple_1:
    print(items)


'''STRINGS'''

print("Create a string and assign it to a variable")
string_1 = "My string"
print(string_1)


print("Find the length of the string")
print(len(string_1))


print("Find the value of an character in the string a specific index")
print(string_1[3])


print("Check whether an item is in the string")
if "y" in string_1:
    print("found")


print("Check whether an item is in the string")
print("y" in string_1)

print("Concatenate (add) two strings together")
string_2 = "Hello"
print(string_2 + " " + string_1)
print(string_2,  string_1)


print("Create an f-string")
print(f"f-string: {string_2}, {string_1}")


print("Split a string using .split")
string_3 = string_1.split()
print(string_3)


print("Join a list of strings using .join")
print(" ".join(string_3))


print("Iterate over the string using range, printing out each character and the index")
for i in range(len(string_3)):
    print(f"{i} : {string_3[i]}")


print("Iterate over the string without using range, printing out each character")
for i in string_3:
    print(i)

'''DICTIONARIES'''

print("Create a dictionary and assign it to a variable")
my_coffee = {
    "type_1" : "Latte", "type_2": "Americano", "type_3": "Flat white", "type_4": "Espresso"
}
print(my_coffee)


print("Find the length of the dictionary")
print(len(my_coffee))


print("Add a new key/value pair")
my_coffee["type_4"] = "Cappuchi"
print(my_coffee)


print("Replace value for a given key")
my_coffee["type_4"] = "Cappuchino"
print(my_coffee)


print("Check whether a key is in the dictionary")
if "type_4" in my_coffee:
    print("found")
print("type_4" in my_coffee) # return True if it in the dict


print("Iterate over keys, printing each key")
for i in my_coffee.keys():
    print(i)


print("Iterate over over key/value pairs using .items(), printing each key and value")
for c_type, name in my_coffee.items():
    print(f"Menu: {c_type} - {name}")


'''SETS'''

print("Create a set and assign it to a variable")
set_1 = {"App", "ss", "MM"}
print(set_1)


print("Find the length of the set")
print(len(set_1))


print("Add a new element")
set_1.add("Nn")
print(set_1)


print("Remove an element")
set_1.remove("Nn")
print(set_1)


print("Check whether a element is in the set")
print("ss" in set_1)


print("Iterate over elements, printing each one out")
for i in set_1:
    print(i)


'''NUMBERS'''

print("Add / subtract / multiply 2 numbers")
a = 5
b = 6
c = a + b
d = c - a
e = d * c
print(f"a = {a}, b ={b} c = {c}, d = {d}, e = {e}")


print("Divide two numbers using normal (float) division")
f = 2
h = a / f
print(f"h: {a} / {f} = {h}")


print("Divide two numbers using integer division")
j = a // f
print(j)


print("Find the modulo (remainder) of two numbers")
print( 5 % 2)


print("Check whether a number is even/odd")
num = 5
if num % 2 == 0:
    print ("Even") #  if the number divided by 2 has a remainder of 0 it's even otherwise odd
else:
    print ("odd")


print("Round a float down to an int")
num_2 = 2.7
print(round(num_2))


'''FUNCTIONS'''

# Write a function that takes no arguments and call it
def new_func():
    pass
print(new_func())

# Write a function that takes one or more arguments and call it
def new_func_with_arg(A , B):
    print(A, B)
print(new_func_with_arg("aa" , "bb"))


# Write a function that returns a value. Call the function and store the return value in a variable
def new_func_with_arg_return(A , B):
    return (A, B)
print(new_func_with_arg_return("aa" , "bb"))


'''LOOPS'''

# Write a while loop
while True:
    print ("Hello")
    break

# Write a for loop that loops a set number of times (e.g. 10 times)
for i in range(0, 10):
    i = "Hello"
    print (i)
    

'''CONDITIONALS'''

# Write an if/elif/else statement
coffee = "Dip"
if coffee not in my_coffee.values():
    my_coffee["type_5"] = coffee
    print(f"{coffee} was added to my_coffee as type_5.")
elif coffee in my_coffee.values():
    print(f"{coffee} is already in your coffee list.")
else:
    print("Please check the input.")
print(my_coffee)


# Write conditionals for the following operators:
a = 6
b = 2
c = 6
# ==
if a == b:
    print("==")
# !=
elif a != b:
    print ("!=")
# <
if a < b:
    print("<")
# >
else:
    print(">")
# <=
if a <= c:
    print(f"{a} <= {c}")
# >=
else:
    print(">=")


'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
nested_list = [["Hello", "N"], ["World", 2]]
print(nested_list)

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second+
print(nested_list[1][0])

# Iterate through the nested data structure using range
for i in range(len(nested_list)):
    print(i)
    for ind in range(len(nested_list[i])):
        print(nested_list[i][ind])
#print(nested_list)


print("Iterate through the nested data structure without using range") 
for i in nested_list:
    for x in i:
        print(x)



'''REMINDER'''

# You're doing great and you got this!
