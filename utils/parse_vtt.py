import re, sys
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    content = f.read()
lines = []
for match in re.finditer(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> .+\n(.+)', content):
    ts = match.group(1)
    text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
    if text and not text.isspace():
        mins = int(ts[3:5])
        secs = int(ts[6:8])
        lines.append(f'{mins}:{secs:02d} {text}')
clean = []
prev = ''
for line in lines:
    text = line.split(' ', 1)[1]
    if text != prev:
        clean.append(line)
        prev = text
print('\n'.join(clean))
