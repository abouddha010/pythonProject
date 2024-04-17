names = ["amu", "anew", "Adu", "Adhvik", "Arindom", "Amita"]

print(names)

print(names[1])



#get a range.. this excludes the last index

print(names[0:4])

print("Let's fetch the list from other end using negavite index")
print(names[-2])

#performing different actions other than replace doesn't change the actual list
print(names)


#replacing the value
names[0] = "Mumma"
print(names)
