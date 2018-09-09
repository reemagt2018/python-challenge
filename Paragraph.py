import re


sentenceList =[]

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''

    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    #print  (sentenceList)
    return sentenceList

#paragraph=input("Enter Paragraph")
# paragraph="Life is one huge emotional mind game. There are days we wake up with an empty heart wondering if we’re even going to make it. We get beaten to the ground over and over again, we get our hope torn from us, we scream at the top of our lungs to the sky hoping that the moon will fill the void that still remains.. But somehow through all the pain, through all the suffering.. These moments never compare to the seconds that take our breath away. The situations given to us that remind us of how beautiful life can be. Let go.. Detach yourself.. There’s too much beauty to quit. I live for moments like these… WE live for moments like these."

fh=open('Parag_Input.txt')
# print (fh.readlines())

paragraphin= fh.readlines()
#print (paragraphin)

paragraph = ''.join(paragraphin)


sentences = splitParagraphIntoSentences(paragraph)
#print (sentences)
numberofsentences=len(list(sentences))
#print (numberofsentences)
char=0
word=1
for s in sentences:

  for i in s:
      char=char+1
      if(i==' '):
            word=word+1

print (" Paragraph Analysis ")
print ("-------------------")
print(f'Approximate Word Count :  {word} ')
#print(word)
# print("Number of characters in the paragraph:")
# print(char)
print (f'Approximate Sentence Count : {numberofsentences}')
#print(numberofsentences)
print (f'Average Letter Count : {char/word}' )
#print (char/word)
print (f'Average Sentence Length : {word/numberofsentences} ')
#print (word/numberofsentences)



#
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
