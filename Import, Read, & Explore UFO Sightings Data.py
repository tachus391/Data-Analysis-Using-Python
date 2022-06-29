'''
1. Import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''
filepath = "ufo-sightings.csv"
ufosightings = [] 

# your code here
import csv
with open('ufo-sightings.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    print(type(reader))
    print(reader.fieldnames)
    for row in reader:
        ufosightings.append(row)

'''
2. How many sightings were there in total?  Put the count in "ufosightings_count" and print the result.
'''
# your code here
ufosightings_count= len(ufosightings)

'''
3. How many sightings were there in the US?  Put the US sightings in "sightings_us" and print.

Hint: Check for ufo sightings where the country is 'us'.

'''

# your code here
sightings_us= [row for row in ufosightings if row["country"] == "us"]

'''
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''

#First, define a Python function that checks if a given duration (seconds) is "valid"
def is_valid_duration(duration_as_string):
# your code here
    try:
        second = float(duration_as_string) #try casting given string to int
    except ValueError:
        
        return False #return False if a ValueError is generated
    
    else:
        
        return second > 10 #return the year itself, if it's greater than 1400

fball = [row for row in sightings_us if (row["shape"] == "fireball") and (is_valid_duration(row["duration (seconds)"]))]


'''
5. Sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''

# your code here
fballsorted= sorted(fball, key= lambda x: float(x['duration (seconds)']), reverse= True)
print (fballsorted)


'''
6. What state had the longest lasting "fireball"?   Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''

# your code here
states = max(fballsorted, key= lambda x: float(x['duration (seconds)']))
print(states)
state= states['state']
print(state)


'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
Write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings
Note: Consider all sightings stored in "ufosightings".

'''
def is_valid_durationzz(duration_as_string):
# your code here
    try:
        second = float(duration_as_string) #try casting given string to int
    except ValueError:
        
        return False #return False if a ValueError is generated
    
    else:
        
        return second > 0 #return the year itself, if it's greater than 1400
# your code here
ufos = [row for row in ufosightings if (is_valid_durationzz(row["duration (seconds)"]))]
durationzz = min(ufos, key= lambda x: float(x['duration (seconds)']))
min_duration= float(durationzz['duration (seconds)'])
print(min_duration)
print(durationzz)

'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

#Create a new list containing values from the "shape" column in ufosightings.
# your code here
sightings_shapes=[]
for row in ufosightings:
    sightings_shapes.append(row['shape'])
#Create a new dictionary with values of that column as keys and the counts as values.
# your code here
count={}
for row in sightings_shapes:
    if row not in count:
        count[row] = 1
    else:
        count[row] += 1
#print(count)   
#Get a list of the dictionary keys and values (use the items() method) and sort them in reverse order, from greatest (most sightings) to least.
#Get and print the top 3.
# your code here
sorted_d = ( sorted(count.items(),key=lambda x: x[1],reverse=True))
#print(sorted_d)
top3shapes=([row for row in sorted_d] [:3])
print(top3shapes)

