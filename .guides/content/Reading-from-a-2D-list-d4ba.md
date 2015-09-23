{Run the code}(python 1-overview/read.py)

On the left we have some code that does the following.

## Define and populate an array
```python
people = [ 
  ['Name', 'Age', 'Color', 'Car'], 
  ['Alice',23,'Blue','Audi'],
  ['Tariq',18,'Red','Mini'], 
  ['Bob',31,'Green','Renault'] 
]
```

There is no need to write this python like this. It could all be on one line but we added the line breaks to make it more readable.

## Lengths
Python makes looping through lists easy, but if you do want to find out how many elements are in a list use the `len()` function.

## Loop through everything
You can see that we actually have a *nested loop* inside another loop.

- The first loop iterates through each *row*. So when it enters the loop for the first time, it is grabbing Alice's data.
- The second loop then loops through all the *columns* and builds up a single string for us to output after processing each row.

