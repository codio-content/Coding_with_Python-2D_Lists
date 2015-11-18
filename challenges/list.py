# Get our list from the command line arguments
import sys
numbers= sys.argv[1:]

# Convert the command line arguments into 2d list
for i in range(0,len(numbers)): 
  numbers[i]= numbers[i].split(',')
  
# Write your code below
