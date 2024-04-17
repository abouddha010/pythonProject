Name ="Amita"

print(Name.isupper())
print("Let's print this in upper case: "+ Name.upper())


print("Checkout these methods for list")

names = ["Amita", "amu"]

names.append("Mumma")
print(names)

names.insert(1, "CutuMumma")
print(names)

names.remove("Amita")
print(names)

#now check if the value exists under list, it will return the boolena value

print("Amita" in names)

#To find the elements in list try Length function
print(names)
print("Elements in this list are: "+ str(len(names)))


#you can empty a list using clear method
listtest = ["1", "2"]
print(listtest)
print(listtest.clear())