
# Get our arguments from the command line
import sys
A= int(sys.argv[1])
B= int(sys.argv[2])

# Your code goes here
data = []

for x in range(0, A):
  data.append([])
  
  for y in range(0, B):
    data[x].append('R' + str(x) + 'C' + str(y))

print(data)