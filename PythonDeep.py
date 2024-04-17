#Finding index and word in a string
sentence = "All about this morning"
print(sentence.find("about"))
print(sentence.find("monday"))
print("this" in sentence)

#varibale stores the new data, but if you modify the string that will be stored as a new string
abc = 6
abc =7
print(abc)

#conversion
print(int(abc))
lmn = int(abc)
lmn+=lmn
print(lmn)

#mathmetical operators
x= 10
y = 40
z = x+y
print(z)
print(y/x) #this provides decimal value
print(y//x) #this will provide the whole int value
print(y%x) #provides reminder


x= 40.5
print(x)
print(x==y)
print(y>x)
print(x!=y)
print(y*x)

print("let's try some logical operators like and or etc.")
print(x>5 and x<12)
print(x>5 or x<12)
print(not x>12) #to return opposite of actual result