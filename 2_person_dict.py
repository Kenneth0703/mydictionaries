person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}



# print out the name of the second child
print(person["children"][1])
# #print out the name of the cat
print(person["pets"]["cat"])
#iterate through all children and print out each child:
kid = person["children"] 
x = 0
for name in kid:
    print(kid[x])
    x = x +1

# print out the pets in this format:
for x,y in person["pets"].items():
    print(f"a {x} named {y}")
# type of pet: dog name of the pet Fido
print(person["pets"]["dog"])