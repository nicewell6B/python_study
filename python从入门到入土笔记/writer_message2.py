from pathlib import Path

contents = 'I love programming\n'
contents += 'I love creat new game.\n'
contents += 'I also love working with data.\n'

path = Path('programming.txt')
path.write_text(contents)