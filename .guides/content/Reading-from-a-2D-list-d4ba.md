{Run the code}(python content/1-overview/read.py)

Have a look at the code on the left. This is what it does:

## Define and populate a list
```python
desks= [
  ['Adam', 'Ben', 'Carl', 'David'],
  ['Edward', 'Frank', 'Georgia', 'Helen'],
  ['Isabelle', 'Joan', 'Kelly', 'Linda']
];
```

There is no need to write the code like this. It could all be on one line but the line breaks were added to make it more readable.

## Lengths
Python makes looping through lists easy, however, if you do want to find out how many elements are in a list use the `len()` function.

## Loop through everything
You can see that we actually have a *nested loop* inside another loop.

`for row in desks:`
- The first loop iterates through each *row*. So when it enters the loop for the first time, it is grabbing the data for the first row.

` for col in row:`
- The second loop then loops through all the *columns*.

