file = open("song.txt","r")
song = file.read()
song = song.split()

count = dict()

for word in song:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

numOfUniqueWords = 0
for word in count:
    if count[word] == 1:
        numOfUniqueWords += 1
print(numOfUniqueWords)

file.close()