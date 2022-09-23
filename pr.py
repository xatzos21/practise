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


list = ["a", "b", "c", "d", "e"]
print(list)
for i in range(len(list)):
    if list[i] == "b":
        list[i] = "B"
print(list)