import re, sys, logging, os, time, traceback

f = open('wordcount.txt', 'r')
reader = f.read()
splitter = reader.split()

#Word Count
wordlist = []
for i in splitter:
	wordlist.append(i)

print 'Total word count: ' + str(len(wordlist))

#Unique Words
uniquelist = []
for i in splitter:
	if i not in uniquelist:
		uniquelist.append(i)

print 'Unique words: ' + str(len(uniquelist))

#Number of Sentences
sentencelist = []
for i in reader:
	if i == "?" or i == "." or i == "!":
		sentencelist.append(i)

print 'Sentences: ' + str(len(sentencelist))

#Brownie Points
#1
print 'Average sentence length in words is: ' + str(len(wordlist) / len(sentencelist))
#3
sortedlist = []
for i in uniquelist:
	if i[-1].isalpha():
		sortedlist.append(str(len(re.findall(i, reader)))+ ' ' + i)

print sorted(sortedlist, reverse=True)