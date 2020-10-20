import SCnlp
import sys
from nltk.tokenize import sent_tokenize
import nltk
local_corenlp_path = 'stanford-corenlp-4.0.0/stanford-corenlp-4.0.0'

with open('input.txt', 'r') as infile, \
        open('input_processato.txt', 'w') as outfile:
  data = infile.read()
  #data = data.replace(".", "")
  data = data.replace(",", "")
  outfile.write(data)

'''
text = open('input_processato.txt', 'r')
lines = text.readlines()
input = ''
for i in lines:
  input = input + i
'''

nltk.download('punkt')
text = open("input_processato.txt").read()
sentences = sent_tokenize(text)


#sys.stdout = open("output.txt", "w")


target = open('target.txt', 'w')
for input in sentences:
    print("REGOLA 1")
    print('\n')
    targ = SCnlp.R1(local_corenlp_path, input)
    for element in targ:
        target.write(element)
        target.write('\n')

target.close()

opinion = open('opinion.txt', 'w')
target = 'target.txt'
for input in sentences:
    print("REGOLA 2")
    print('\n')
    opin = SCnlp.R2(local_corenlp_path, input, target)
    for element in opin:
        opinion.write(element)
        opinion.write('\n')

opinion.close()

#sys.stdout.close()

target = open('target.txt', 'a')
targe = 'target.txt'
for input in sentences:
    print("REGOLA 3")
    print('\n')
    targ = SCnlp.R3(local_corenlp_path, input, targe)
    for element in targ:
        target.write(element)
        target.write('\n')

target.close()

opinion = open('opinion.txt', 'a')
opin = 'opinion.txt'
for input in sentences:
    print("REGOLA 4")
    print('\n')
    op = SCnlp.R4(local_corenlp_path, input, opin)
    for element in op:
        opinion.write(element)
        opinion.write('\n')

opinion.close()

