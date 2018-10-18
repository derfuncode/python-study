words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w)>6:
        words.insert(1,w)
print(words)

for w in words:
    print(w,len(w))

