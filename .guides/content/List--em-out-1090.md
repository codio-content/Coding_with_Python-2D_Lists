{Check It!|assessment}(test-3455473410)

|||guidance
### Solution
```python
# Get our list from the command line arguments
import sys
numbers= sys.argv[1:]

# Convert the command line arguments into 2d list
for i in range(0,len(numbers)): 
  numbers[i]= numbers[i].split(',')
  
# Write your code below
gtotal = 0                    # initialize the grand total

for row in numbers:           # for each row
  total = 0                   # reset this row total
  for col in row:             # for each col
    total = total + int(col)  # total up the row
    
  print(total)                # print the row total
  gtotal = gtotal + total     # tract the grand total

print(gtotal)                 # print the grand total
```
|||
