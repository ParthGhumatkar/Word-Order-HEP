n = int(input())
counter = {}
words = []

for i in range(n):
  word = input()
  words.append(word)
  if word in counter:
    counter[word] += 1
  else:
    counter[word] = 1
    
print(len(counter))
print(' '.join([str(counter[word]) for word in counter]))
