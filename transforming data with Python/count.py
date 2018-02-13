import read
from collections import Counter
data = read.load_data()
heads = data.headline
s = ''
for h in heads:
    s = s + str(h)
    
print(Counter(s.lower().split()).most_common())
    