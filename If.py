# In Python we don't use {} curly braces, only indentation is required
# In Python to pass string under print we can either use single or double qoutes
# both are fine but check the example below to understand why we need both

print("it's a hot day")

#if we use single quotes on the above sentence Python will get confused,
# because we already have one single quote as part of sentence and wise versa


Temparture = 9
if Temparture>30:
    print("Drink plenty of water")
elif Temparture>=20:
    print("It's a perfect day")
elif Temparture >=10:
    print("It's a bit cold")
else:
    print("It's freezing Today")
print("This is not part of if block due to indentation, so this gonna execute anyway")

