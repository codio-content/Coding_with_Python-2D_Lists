
# Creating a 2D list
people = [ 
  ['Alice',23,'Blue','Audi'],
  ['Tariq',18,'Red','Mini'], 
  ['Bob',31,'Green','Renault'] 
]

# Looping through both dimensions
for row in people:
  print('this row has ' + str(len(row)) + ' items')
  
  for col in row:
    print(col)
  
  print('---')
