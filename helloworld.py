print("Hello, World!")
x = ["a", 'b', 'c']
for i in x:
    print(i)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "paw"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# #  list comprehension 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


even = [x for x in range(1,50) if x % 2 == 0]
print(even)

odd = [x for x in range(50, 1, -1) if x % 2 != 0]
print(odd)