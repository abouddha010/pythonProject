#range ..range(5) is equivelant ti range(0,5), while printing range excludes the last no.

numbers = range(5)

for number in numbers:
    print(number)


print("Now try this")

newnumbers = range(5,10)
for numbernew in newnumbers:
    print(numbernew)

print("Now try this with interval/steps")

newnumbers1 = range(2,10, 2)
for numbernew1 in newnumbers1:
    print(numbernew1)