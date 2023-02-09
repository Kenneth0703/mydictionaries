'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''
# earthquake = shake["features"][1]["properties"]


import json

infile = open("eq_data.json", "r")
shake =json.load(infile)

# total number of earthquakes
print(shake["metadata"]["count"])
# it uses the count feature in the code might need to change later to actually count_
x = 0 

earthquake = shake["features"] 
y = 0

for x in earthquake:
   mag = earthquake[y]["properties"]["mag"]
   y = y + 1
   if mag >6:
      x = y -1
      
      Location = earthquake[x]["properties"]["place"]
      Longitude = earthquake[x]["geometry"]["coordinates"][0]
      Latitude = earthquake[x]["geometry"]["coordinates"][1]

      eq_dict = {(print(f"Location: {Location}")):[
      (print(f"Magnitude: {mag}")),
      (print(f"Longitude: {Longitude}")),
      (print(f"Latitude: {Latitude}")),
       print(),
       print()
         ]}


print(eq_dict)
