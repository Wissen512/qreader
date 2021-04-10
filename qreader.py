import os
import time

file = open("text.txt", "r")
text = file.read()
file.close()

words = []
word = ''

os.system("clear")

for i in range(len(text)):
	if text[i] in ' .,\n':
		words.append(word)
		word = ''

		if text[i] in '.,':
			i += 2
		else:
			i += 1
	else:
		word += text[i]


#print(word)
#print(words)

while True:
    for i in range(len(words)):
    	print(words[i])
    	time.sleep(0.2)
    	os.system("clear")

