from pathlib import Path

path = Path('百万富翁快车道 (【美】MJ·德马科) (Z-Library)1.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('sorry, thr file {path} not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file{path} has {num_words} words.')#因为中文没有空格所以这方法算不了中文的字数
