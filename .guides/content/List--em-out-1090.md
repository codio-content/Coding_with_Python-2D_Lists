{Run the code}(python3 run-user.py list.py)

{Check It!|assessment}(test-3455473410)

|||guidance
### Solution
```python
input0 = input0([ 
  [1,2,3,4],
  [9,8,7,6], 
  [11,12] 
])

gtotal = 0

for row in input0:
  total = 0
  
  for col in row:
    total = total + col
    
  output(total)
  gtotal = gtotal + total

output(gtotal)
```
|||