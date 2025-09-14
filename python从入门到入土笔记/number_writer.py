from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5, 6]
path = Path('numbers.json')
with path.open('w', encoding='utf-8') as f:
    json.dump(numbers, f)

'''
or
contents = json.dump(numbers)
path.write_text(contents)
'''