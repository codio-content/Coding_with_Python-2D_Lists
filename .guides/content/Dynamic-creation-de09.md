{Run the code}(python run-user.py dynamic.py)

{Check It!|assessment}(test-667129063)

|||guidance
### Solution
```python
input0 = input0(2)
input1 = input1(8)

data = []

for x in range(0, input0):
  data.append([])
  
  for y in range(0, input1):
    data[x].append('R' + str(x) + 'C' + str(y))

output(data)
```
|||