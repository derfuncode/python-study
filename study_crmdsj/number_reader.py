import json
filename = 'numbers.json'

with open(filename) as f1:
    numbers = json.load(f1)

print(numbers)
