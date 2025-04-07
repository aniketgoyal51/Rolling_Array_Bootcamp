list1=[1,2,3,4]
list2=["banana","apple","orange","grapes"]

# list1.extend(list2)
# print(list1)
list2.insert(1,"kiwi")
list1.append(5)
print(len(list2))
print(list2)
print(list1)

list2.remove("kiwi")
print(list2)

# list1.clear()
# print(list1)

print(list2.index("kiwi"))
print(list2.count("kiwi"))

print(list1.reverse())  # and same for asceding(sort)

del list2[1] # same thing pop do