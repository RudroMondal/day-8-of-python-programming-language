# stap 1:Creat a dictionary
vehicles ={}

# stap 2:Add 'key' and 'value' in dictionary
vehicles["Car"]="black"
vehicles["Bike"]="red"
vehicles["Auto"]="yellow"

# stap 3:Update the color of "Bike" in the `vehicles`
vehicles["Bike"]="blue"

# stap 4:Delete the "Auto" from the `vehicles` dictionary.
del vehicles["Auto"]

#clean all dictionary 
vehicles.clear()

# print vehicles
print(vehicles)