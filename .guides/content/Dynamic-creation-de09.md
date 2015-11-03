{Check It!|assessment}(test-667129063)

|||guidance
### Solution
```python
# Get our arguments from the command line
A= sys.argv[2]
B= sys.argv[3]

# Your code goes here
data = []

for x in range(0, A):
  data.append([])
  
  for y in range(0, B):
    data[x].append('R' + str(x) + 'C' + str(y))

print(data)
```
|||
