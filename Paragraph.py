import re


sentenceList =[]

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''

    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    print  (sentenceList)
    return sentenceList

paragraph=input("Enter Paragraph")

sentences = splitParagraphIntoSentences(paragraph)
print (sentences)
numberofsentences=len(list(sentences))
print (numberofsentences)
char=0
word=1
for s in sentences:

  for i in s:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the paragraph:")
print(word)
print("Number of characters in the paragraph:")
print(char)
print ("Number of sentences")
print(numberofsentences)
print ("Average Letter Count")
print (char/word)
print ("Average Sentence Length")
print (word/numberofsentences)
