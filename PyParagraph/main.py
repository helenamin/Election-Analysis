# Module to create file paths across operating systems
import os

import re

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
passageFile = os.path.join(dirname,"input.txt")

#Path to write the result
output_path = os.path.join(dirname,"analysis","result.txt")

word_characters=0
Average_Letter_Count= 0
Average_Sentence_Length =0


textfile = open(passageFile,'rt')
data = textfile.read()
words = data.split()
sentences = re.split("(?<=[.!?]) +",data)

for word in words:
    word_characters += len(word)

Average_Letter_Count = round((word_characters/len(words)),1)

Average_Sentence_Length = round((len(words)/len(sentences)),1)


print(len(words),"  ",len(sentences),"  ",Average_Letter_Count,"  ",Average_Sentence_Length)


message = f"\nParagraph Analysis\n----------------------------\
    \nApproximate Word Count: {len(words)}\
    \nApproximate Sentence Count: {len(sentences)}\
    \nAverage Letter Count: {Average_Letter_Count}\
    \nAverage Sentence Length: {Average_Sentence_Length}"





#print Paragraph Analysis result into terminal
print(message)

#write the result into result.txt file
outF = open(output_path,'w')
# Write result using writelines()
outF.writelines(message)
outF.close()