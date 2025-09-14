from pathlib import Path

path = Path('百万富翁快车道 (【美】MJ·德马科) (Z-Library).txt')
contents = path.read_text('utf-8').rstrip()

print(contents)
