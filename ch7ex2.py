names_set = set()
print("Enter names to be saved in the set")
while True:
    name = input("Enter a name : ")
    if name == "":
        break
    if name in names_set:
        print("You Entered an Existing name")
    else:
        print("You Entered a New name")
        names_set.add(name)

print("\nEntered Names are:")
for name in names_set:
    print(name)


