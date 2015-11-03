# Get our list from the command line arguments
numbers= sys.argv[2]

# Write your code below
gtotal = 0

for row in numbers:
  total = 0
  
  for col in row:
    total = total + col
    
  print(total)
  gtotal = gtotal + total

print(gtotal)
