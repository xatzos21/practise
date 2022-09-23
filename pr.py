# Task is by using an index
# to replace "Peer" with "Malcom X"

# Add two names to the list of names

# Experiment with the methods in a list using dir(names)

names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]
print(names)
names[5] = "Malcom X"
print(names)
names.append("Martin")
print(names)
names.insert(1, "Patty")
print(names)


numbers = [2, 4, 6, 8, 10]
print(numbers)
numbers[1] = int(input("Choose new number: "))
numbers[4] = int(input("Choose another number: "))
print(numbers)


list1 = ["a", "b", "c", "d", "e"]
print(list1)
for i in range(len(list1)):
    if list1[i] == "b":
        list1[i] = "B"
print(list1)

x = list1.index("B")
print(x)
list1 = list1[:x]+["b"]+list1[x+1:]
print(list1)

