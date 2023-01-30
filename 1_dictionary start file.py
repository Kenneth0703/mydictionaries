import random

phonebook = {}  # empty dict
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

name = "chris"

# if name in phonebook:                       # looks through all the keys for a match there are methods you can use
#     print(phonebook[name])
# else:
#     print(f"{name} is not in the phonebook")



#print(phonebook['Chris'])                   # is case sensitive
# print(phone)                                # keyError means it did not find a match to that key

# mydictionary = dict(m=8,n=9)
# print(mydictionary)

# print(len(phonebook))   
# print(type(phonebook))

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()



""""""



print()
print('*****  end section 2 ********')
print()


# print(phonebook)







print()
print('*****  start section 3 - edit/append dictionary ********')
print()


# phonebook['Chris'] = "555-0123"
# phonebook["Joe"] = "555-4444"


print()
print('*****  end section 3 ********')
print()



""""""


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


# print(phonebook)

# del phonebook['Chris']

# print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


# for key in phonebook:        # key is variable name key is called the iterator 
#     print(f"the key is the {key} and the value is {phonebook[key]}")   #### very iportant, to get phonenumber you need the key 

# for value in phonebook.values():       # this gives you all the phone numbers
#     print(value)


# for key, value in phonebook.items():
#      print(f"the key is the {key} and the value is {value}")

# for ph_tuple in phonebook.items():          # this makes it a tuple which  is not mutible
#     print(ph_tuple)


print()
print('*****  end section 5 ********')
print()


""""""

print()
print('*****  start section 6 - using get and clear ********')
print()


# phone = phonebook.get("Chris","999")   # default number of 999
# print(phone)

# phonebook.clear()           # empty DICT



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()
# pop method pops a key vlue paire out of the dict and saves in a varoable

# remove = phonebook.pop("Chris", "not found")
# print(remove)
# print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()
# # random part does not work
# # only pops out last item IE joanne 
# # there is a workaround using lists
# a =phonebook.popitem()

# print(a)
# print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

# phonebook_list = list(phonebook)  # using list on DICT, default option is the KEY 
# print(phonebook_list)    # list of the keys
# random_key = random.choice(phonebook_list)             # random . choice only works on list
# print(random_key)
# print(phonebook[random_key])
# rewrite in one line
# print(phonebook[random.choice(list(phonebook)])) 
print(phonebook[random.choice(list(phonebook))])   # this is prefered becausee it uses less variables

print()
print('*****  end section 9 ********')
print()







