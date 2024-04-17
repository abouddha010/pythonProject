# let's try this program where you have to provide your weight,
# then program will ask if it is in Kilo gram or pounds, and print the output in kilo grams
print("please enter you weight here: ")
weightNumber = input()
print("Your weight is: " +weightNumber)

print("Could you tell me if it is in KG(k), Pounds(lb) or in other unit: " )
weightUnit = input()
print("entered weight unit is: "+weightUnit)


if weightUnit == "k" or weightUnit == "K":
    print("weight in KGs is: "+weightNumber)
elif weightUnit == "l" or weightUnit == "L":
    intFormWeight = int(weightNumber)
    weightNumberNew = str(intFormWeight*0.45) #To convert Pound into KGs
    print("Convered weight in KGs is: " + weightNumberNew)
else:
    print("you have entered an invalid unit")
print("Weight should get printed only in KGs")